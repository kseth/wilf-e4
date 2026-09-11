#include <array>
#include <bitset>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
using namespace std;
using Bits=bitset<343>;
struct Prof {array<int,7> row;int hx,hy,code;array<Bits,3> mask;vector<pair<int,int>> corners;};
vector<Prof> allp;
Bits delta,erodecap,fx,fy,fz,bx,by,bz;array<Bits,7> layers;
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
 ofstream out(dir+"/weighted_candidates_sample.tsv"),fails(dir+"/unit_failures.tsv"),stats(dir+"/enumeration.jsonl");
 out<<"pid\txy\txz\tyz\tm\tdegree\tunit_D\terosion\n";fails<<"pid\txy\txz\tyz\tm\tdegree\tunit_D\terosion\n";
 for(int x=0;x<7;x++)for(int y=0;y<7;y++)for(int z=0;z<7;z++){
  int i=idx(x,y,z),d=x+y+z;
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
  mt19937_64 rng(20260910+pid);vector<array<int,8>> sample;
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
    array<int,8> record={pid,a->code,b->code,c->code,m,R,D,e};
    if(sample.size()<5000)sample.push_back(record);else {auto pick=rng()%remaining;if(pick<5000)sample[pick]=record;}
    if(10*D<10*m-29){unitfails++;fails<<pid<<'\t'<<a->code<<'\t'<<b->code<<'\t'<<c->code<<'\t'<<m<<'\t'<<R<<'\t'<<D<<'\t'<<e<<'\n';}
   }
  }
  for(auto record:sample){for(int i=0;i<8;i++)out<<record[i]<<(i==7?'\n':'\t');}
  stats<<"{\"pid\":"<<pid<<",\"corner\":["<<p[0]<<","<<p[1]<<","<<p[2]<<"],\"compatible\":"<<compatible<<",\"degree_ok\":"<<degreeok<<",\"m30\":"<<m30<<",\"erosion_ok\":"<<erosionok<<",\"q_ok\":"<<qok<<",\"six_maxima\":"<<sixmax<<",\"remaining\":"<<remaining<<",\"unit_failures\":"<<unitfails<<",\"max_m_pre_erosion\":"<<maxm<<",\"smallest_tenth_margin\":"<<smallestMargin<<",\"histogram\":{";
  bool first=true;for(int m=30;m<85;m++)if(hist[m]){if(!first)stats<<",";first=false;stats<<"\""<<m<<"\":"<<hist[m];}stats<<"}}\n";stats.flush();
  cerr<<"pid="<<pid<<" compatible="<<compatible<<" degree="<<degreeok<<" m30="<<m30<<" erosion="<<erosionok<<" qok="<<qok<<" six="<<sixmax<<" remaining="<<remaining<<" unitfails="<<unitfails<<" margin10="<<smallestMargin<<"\n";
 }
}
