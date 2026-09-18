// Independent finite brute force: three coordinate-plane lower ideals.
// This file contains no center/horn decomposition or nested-section recurrence.
#include <algorithm>
#include <array>
#include <functional>
#include <iostream>
#include <limits>
#include <vector>
using I=long long;
struct Profile {std::vector<int> height; int nx,ny;};
std::vector<Profile> profiles(I wi,I wj,I cap,int pi,int pj){
 int nx=int(cap/wi)+1;std::vector<int> r(nx);std::vector<Profile> out;
 std::function<void(int,int)> rec=[&](int x,int prev){
  if(x==nx){if(pi>=nx||r[pi]<=pj)return;int count=0;for(int y:r)count+=y>0;out.push_back({r,count,r[0]});return;}
  int allowed=std::min<int>(prev,int((cap-wi*x)/wj)+1);
  for(int y=0;y<=allowed;y++){r[x]=y;rec(x+1,y);}
 };
 rec(0,int(cap/wj)+1);return out;
}
int main(){I q,B0,C0,H0,B1,C1,H1;int px,py,pz;
 while(std::cin>>q>>B0>>C0>>H0>>B1>>C1>>H1>>px>>py>>pz){
  auto xy=profiles(q,B0,H1,px,py),xz=profiles(q,C0,H1,px,pz),yz=profiles(B0,C0,H1,py,pz);
  I best=std::numeric_limits<I>::min(),compatible=0,feasible=0,totalpoints=0;
  for(auto &a:xy)for(auto &b:xz){if(a.nx!=b.nx)continue;for(auto &c:yz){if(a.ny!=c.nx||b.ny!=c.ny)continue;compatible++;
    I score=0,points=0;bool ok=true;
    for(int x=0;x<a.nx&&ok;x++)for(int y=0;y<a.height[x]&&ok;y++){
      int bound=std::min(b.height[x],c.height[y]);
      if(x>=px&&y>=py)bound=std::min(bound,pz);
      if(bound&&q*x+B0*y+C0*(bound-1)>H1){ok=false;break;}
      for(int z=0;z<bound;z++){score+=4*(q*x+B1*y+C1*z)+q-3*H0;points++;}
    }
    if(ok){feasible++;totalpoints+=points;best=std::max(best,score);}
  }}
  std::cout<<best<<' '<<compatible<<' '<<feasible<<' '<<totalpoints<<' '<<xy.size()<<' '<<xz.size()<<' '<<yz.size()<<'\n'<<std::flush;
 }
}
