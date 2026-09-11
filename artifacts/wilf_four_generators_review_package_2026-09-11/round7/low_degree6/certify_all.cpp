#include <array>
#include <bitset>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
using namespace std;
#include "proposing_lp.hpp"
#include "exact_dual.hpp"
using Bits=bitset<343>;
struct Prof {array<int,7> row;int hx,hy,code;array<Bits,3> mask;vector<pair<int,int>> corners;};
vector<Prof> allp;
Bits delta,erodecap,fx,fy,fz,bx,by,bz;array<Bits,7> layers;array<array<Bits,7>,3> coord;
int idx(int x,int y,int z){return 49*x+7*y+z;}
void profiles(array<int,7>&r,int i){
 if(i==7){
  Prof p;p.row=r;p.hx=0;p.hy=r[0];p.code=0;
  for(int x=0;x<7;x++){p.hx+=r[x]>0;p.code|=r[x]<<(3*x);}
  if(p.hx==0)return;
  for(int x=1;x<p.hx;x++)if(r[x]<r[x-1])p.corners.push_back({x,r[x]});
  for(int x=0;x<7;x++)for(int y=0;y<7;y++)for(int z=0;z<7;z++){
   if(y<r[x])p.mask[0].set(idx(x,y,z));
   if(z<r[x])p.mask[1].set(idx(x,y,z));
   if(z<r[y])p.mask[2].set(idx(x,y,z));
  }
  allp.push_back(p);return;
 }
 int cap=min(7-i,i?r[i-1]:7);
 for(int h=0;h<=cap;h++){r[i]=h;profiles(r,i+1);}
}
vector<const Prof*> eligible(int a,int b,int opp){
 vector<const Prof*> out;int P=a+b+opp;
 for(auto &p:allp){
  if(p.row[a]<=b || (int)p.corners.size()>P-2)continue;
  int upper=0;for(auto [x,y]:p.corners)upper+=(x>=a&&y>=b);
  if(upper>opp)continue;
  out.push_back(&p);
 }
 return out;
}
int main(int argc,char**argv){
 string dir=argc>1?argv[1]:"round7/low_degree6";
 ofstream out(dir+"/unused.tsv"),fails(dir+"/certification_failure.tsv"),stats(dir+"/certification.jsonl");
 basis_output.open(dir+"/dual_bases.jsonl");assignment_output.open(dir+"/dual_assignments.bin",ios::binary);
 out<<"pid\txy\txz\tyz\tm\tdegree\tunit_D\terosion\n";fails<<"pid\txy\txz\tyz\tm\tdegree\tunit_D\terosion\n";
 for(int x=0;x<7;x++)for(int y=0;y<7;y++)for(int z=0;z<7;z++){
  int i=idx(x,y,z),d=x+y+z;coord[0][x].set(i);coord[1][y].set(i);coord[2][z].set(i);
  if(d<=6){delta.set(i);layers[d].set(i);}
  if(d<=5)erodecap.set(i);
  if(x==0)fx.set(i);if(y==0)fy.set(i);if(z==0)fz.set(i);
  if(x==6)bx.set(i);if(y==6)by.set(i);if(z==6)bz.set(i);
 }
 array<int,7> row;profiles(row,0);cerr<<"profiles "<<allp.size()<<"\n";
 vector<array<int,3>> ps={{1,1,3},{1,2,2},{1,1,4},{1,2,3},{2,2,2},{1,1,5},{1,2,4},{1,3,3},{2,2,3}};
 for(int pid=0;pid<(int)ps.size();pid++){
  auto p=ps[pid];auto xy=eligible(p[0],p[1],p[2]),xz=eligible(p[0],p[2],p[1]),yz=eligible(p[1],p[2],p[0]);
  array<array<vector<const Prof*>,8>,8> zgroups;
  for(auto c:yz)zgroups[c->hx][c->hy].push_back(c);
  Bits clip;clip.set();for(int x=p[0];x<7;x++)for(int y=p[1];y<7;y++)for(int z=p[2];z<7;z++)clip.reset(idx(x,y,z));
  uint64_t compatible=0,degreeok=0,m30=0,erosionok=0,qok=0,sixmax=0,remaining=0,unitfails=0;
  uint64_t proposals=0,cachehits=0;vector<array<int,4>>recent;long long smallestNum=1000000,smallestDen=1;
  array<uint64_t,85> hist{};int smallestMargin=1000000,maxm=0;
  for(auto a:xy)for(auto b:xz){if(a->hx!=b->hx)continue;
   auto ab=a->mask[0]&b->mask[1]&clip;
   for(auto c:zgroups[a->hy][b->hy]){
    compatible++;auto T=ab&c->mask[2];if((T&~delta).any())continue;degreeok++;
    int m=T.count();maxm=max(maxm,m);if(m<30)continue;m30++;
    auto A=T&(T>>49)&(T>>7)&(T>>1)&erodecap;
    int e=A.count()+(A&fx).count()+(A&fy).count()+(A&fz).count();if(e>m)continue;erosionok++;
    auto F0=T&(~(T>>49)|bx),F1=T&(~(T>>7)|by),F2=T&(~(T>>1)|bz);
    if((F1&F2).count()>2*a->hx || (F0&F2).count()>2*a->hy || (F0&F1).count()>2*b->hy)continue;qok++;
    int maxima=(F0&F1&F2).count();if(maxima<=6){sixmax++;continue;}remaining++;hist[m]++;
    int R=0,sum=0;for(int d=1;d<=6;d++){int cnt=(T&layers[d]).count();if(cnt)R=d;sum+=d*cnt;}
    int D=3*m*R-4*sum;smallestMargin=min(smallestMargin,10*D-10*m+29);
    
    array<int,3>S{};for(int j=0;j<3;j++)for(int k=1;k<=6;k++)S[j]+=k*(T&coord[j][k]).count();
    bool ok=false;long long margin_num=0,denom=1;array<int,4>chosen{};
    for(auto ids:recent){
     bool contained=true;for(int id:ids)if(id<343&&!T.test(id)){contained=false;break;}
     if(contained&&exact_dual(ids,m,S,margin_num,denom)){chosen=ids;ok=true;cachehits++;break;}
    }
    if(!ok){
     proposals++;vector<int>Z;auto K=F0&F1&F2;
     for(size_t index=K._Find_first();index<K.size();index=K._Find_next(index))Z.push_back(index);
     vector<vector<double>>mat;vector<double>rhs;
     for(int id:Z){int x=id/49,y=(id/7)%7,z=id%7;mat.push_back({double(x),double(y),double(z),-1});rhs.push_back(-x-y-z);}
     mat.push_back({0,0,0,1});rhs.push_back(7);
     vector<double>obj={4.0*S[0],4.0*S[1],4.0*S[2],-3.0*m},solution;
     ProposingLP lp(mat,rhs,obj);if(!lp.solve(solution)){cerr<<"LP failure\n";return 2;}
     int at=0;for(int var:lp.N)if(var!=-1){
      if(var<4)chosen[at++]=343+var;
      else {int i=var-4;chosen[at++]=(i<(int)Z.size()?Z[i]:347);}
     }
     if(at!=4){cerr<<"basis size failure\n";return 3;}
     ok=exact_dual(chosen,m,S,margin_num,denom);
     if(!ok){
      fails<<pid<<'\t'<<a->code<<'\t'<<b->code<<'\t'<<c->code<<'\t'<<m<<'\t'<<R<<'\t'<<D<<'\t'<<e<<'\n';
      cerr<<"EXACT CERTIFICATE FAILURE pid="<<pid<<" rows="<<a->code<<","<<b->code<<","<<c->code<<" m="<<m<<" weights="<<solution[0]+1<<","<<solution[1]+1<<","<<solution[2]+1<<" M="<<solution[3]<<" margin="<<margin_num<<"/"<<denom<<"\n";return 4;
     }
     recent.insert(recent.begin(),chosen);if(recent.size()>16)recent.pop_back();
    }
    if(margin_num*smallestDen<smallestNum*denom){smallestNum=margin_num;smallestDen=denom;}
    if(remaining%100000==0){assignment_output.flush();basis_output.flush();cerr<<"progress pid="<<pid<<" checked="<<remaining<<" proposals="<<proposals<<" bases="<<basis_cache.size()<<"\n";}

    if(10*D<10*m-29){unitfails++;fails<<pid<<'\t'<<a->code<<'\t'<<b->code<<'\t'<<c->code<<'\t'<<m<<'\t'<<R<<'\t'<<D<<'\t'<<e<<'\n';}
   }
  }
  
  stats<<"{\"pid\":"<<pid<<",\"corner\":["<<p[0]<<","<<p[1]<<","<<p[2]<<"],\"compatible\":"<<compatible<<",\"degree_ok\":"<<degreeok<<",\"m30\":"<<m30<<",\"erosion_ok\":"<<erosionok<<",\"q_ok\":"<<qok<<",\"six_maxima\":"<<sixmax<<",\"remaining\":"<<remaining<<",\"proposals\":"<<proposals<<",\"cache_hits\":"<<cachehits<<",\"certificate_min_numerator\":"<<smallestNum<<",\"certificate_min_denominator\":"<<smallestDen<<",\"unit_failures\":"<<unitfails<<",\"max_m_pre_erosion\":"<<maxm<<",\"smallest_tenth_margin\":"<<smallestMargin<<",\"histogram\":{";
  bool first=true;for(int m=30;m<85;m++)if(hist[m]){if(!first)stats<<",";first=false;stats<<"\""<<m<<"\":"<<hist[m];}stats<<"}}\n";stats.flush();assignment_output.flush();basis_output.flush();
  cerr<<"pid="<<pid<<" compatible="<<compatible<<" degree="<<degreeok<<" m30="<<m30<<" erosion="<<erosionok<<" qok="<<qok<<" six="<<sixmax<<" remaining="<<remaining<<" proposals="<<proposals<<" bases="<<basis_cache.size()<<" unitfails="<<unitfails<<" margin10="<<smallestMargin<<"\n";
 }
}
