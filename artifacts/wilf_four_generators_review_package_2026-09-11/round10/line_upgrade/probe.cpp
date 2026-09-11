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
 uint64_t tested=0,failures=0;
 ofstream failure("round10/line_upgrade/first_failure.json");
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
    int maxima=(F0&F1&F2).count();if(maxima<=6){sixmax++;}remaining++;hist[m]++;
    int R=0,sum=0;for(int d=1;d<=6;d++){int cnt=(T&layers[d]).count();if(cnt)R=d;sum+=d*cnt;}
    int D=3*m*R-4*sum;smallestMargin=min(smallestMargin,10*D-10*m+29);
    
    vector<array<int,3>> maxima_points;
    auto K=F0&F1&F2;
    for(size_t id=K._Find_first();id<K.size();id=K._Find_next(id))maxima_points.push_back({int(id)/49,(int(id)/7)%7,int(id)%7});
    int gain=0;array<Bits,3> Fs={F0,F1,F2};
    for(int j=0;j<3;j++)for(size_t id=Fs[j]._Find_first();id<Fs[j].size();id=Fs[j]._Find_next(id)){
      array<int,3> t={int(id)/49,(int(id)/7)%7,int(id)%7};
      int topdegree=0;
      for(auto u:maxima_points)if(u[0]>=t[0]&&u[1]>=t[1]&&u[2]>=t[2])topdegree=max(topdegree,u[0]+u[1]+u[2]);
      gain+=(t[j]+1)*(topdegree-t[0]-t[1]-t[2]);
    }
    tested++;
    if(gain<m-2){
      cout<<"FAIL pid="<<pid<<" tested="<<tested<<" m="<<m<<" gain="<<gain<<" degree="<<R<<" codes="<<a->code<<","<<b->code<<","<<c->code<<"\n";
      failure<<"{\"corner\":["<<p[0]<<","<<p[1]<<","<<p[2]<<"],\"m\":"<<m<<",\"gain\":"<<gain<<",\"profile_codes\":["<<a->code<<","<<b->code<<","<<c->code<<"],\"points\":[";
      bool first=true;for(size_t id=T._Find_first();id<T.size();id=T._Find_next(id)){if(!first)failure<<",";first=false;failure<<"["<<id/49<<","<<(id/7)%7<<","<<id%7<<"]";}failure<<"]}\n";
      return 0;
    }
   }
  }
  
  cout<<"pid="<<pid<<" tested="<<tested<<"\n";
 }
}
