// Finite Lemma 2.4: subtractive box moments and prefix-maxima horn DP.
// Input rows: q B0 C0 H0 B1 C1 H1. Output: three (2,1,1)-corner orientation bounds.
#include <algorithm>
#include <array>
#include <iostream>
#include <limits>
#include <vector>
#include <sstream>
#include <stdexcept>
#include <string>
using I=long long;
static_assert(std::numeric_limits<I>::digits >= 63, "64-bit scores required");
static_assert(std::numeric_limits<int>::digits >= 31, "32-bit indices required");

I solve(I q,const std::array<I,3>&lo,const std::array<I,3>&hi,const std::array<int,3>&p){
  std::array<I,3> lw={q,lo[0],lo[1]},uw={q,hi[0],hi[1]};
  std::array<int,3> n; for(int i=0;i<3;i++)n[i]=int(hi[2]/lw[i])+1;
  std::array<std::vector<I>,3> horns;
  std::array<int,3> stride;
  for(int axis=0;axis<3;axis++){
    int other[2],k=0;for(int i=0;i<3;i++)if(i!=axis)other[k++]=i;
    int nb=n[other[0]],nc=n[other[1]];stride[axis]=nc;
    auto index=[nb,nc](int t,int u,int v){return (t*nb+u)*nc+v;};
    auto &H=horns[axis];H.assign((n[axis]+1)*nb*nc,0);
    for(int t=n[axis]-1;t>=0;t--)for(int u=0;u<nb;u++)for(int v=0;v<nc;v++){
      I count=I(u+1)*(v+1);
      I height=lw[axis]*t+lw[other[0]]*u+lw[other[1]]*v;
      I twice=count*(2*uw[axis]*t+uw[other[0]]*u+uw[other[1]]*v);
      if(t>=p[axis]&&u>=p[other[0]]&&v>=p[other[1]]){
        I removed=I(u-p[other[0]]+1)*(v-p[other[1]]+1);count-=removed;
        twice-=removed*(2*uw[axis]*t+uw[other[0]]*(p[other[0]]+u)+uw[other[1]]*(p[other[1]]+v));
        height=lw[axis]*t+std::max(lw[other[0]]*(p[other[0]]-1)+lw[other[1]]*v,lw[other[0]]*u+lw[other[1]]*(p[other[1]]-1));
      }
      I value=0;
      if(height<=hi[2])value=std::max<I>(0,2*twice+count*(q-3*lo[2])+H[index(t+1,u,v)]);
      if(u)value=std::max(value,H[index(t,u-1,v)]);
      if(v)value=std::max(value,H[index(t,u,v-1)]);
      H[index(t,u,v)]=value;
    }
  }
  I best=std::numeric_limits<I>::min();
  for(int a=0;a<n[0];a++)for(int b=0;b<n[1];b++)for(int c=0;c<n[2];c++){
    std::array<int,3>x={a,b,c}; I count=I(a+1)*(b+1)*(c+1),height=0,usum=0;
    for(int i=0;i<3;i++){height+=lw[i]*x[i];usum+=uw[i]*x[i];}
    I twice=count*usum;
    if(a>=p[0]&&b>=p[1]&&c>=p[2]){
      I removed=I(a-p[0]+1)*(b-p[1]+1)*(c-p[2]+1);count-=removed;
      I removed_sum=0;for(int i=0;i<3;i++)removed_sum+=uw[i]*(x[i]+p[i]);
      twice-=removed*removed_sum;I old_height=height;height=0;
      for(int i=0;i<3;i++)height=std::max(height,old_height-lw[i]*(x[i]-p[i]+1));
    }
    if(height>hi[2])continue;
    I value=2*twice+count*(q-3*lo[2]);
    value+=horns[0][((a+1)*n[1]+b)*n[2]+c];
    value+=horns[1][((b+1)*n[0]+a)*n[2]+c];
    value+=horns[2][((c+1)*n[0]+a)*n[1]+b];
    best=std::max(best,value);
  }
  return best;
}


int main(int argc,char**) {
  std::ios::sync_with_stdio(false);std::cin.tie(nullptr);
  try {
    if(argc!=1)throw std::runtime_error("only complete mode supported");
    std::string line;
    while(std::getline(std::cin,line)) {
      I q;std::array<I,3>lo,hi;std::string extra;std::istringstream request(line);
      if(!(request>>q>>lo[0]>>lo[1]>>lo[2]>>hi[0]>>hi[1]>>hi[2])||(request>>extra))
        throw std::runtime_error("malformed request");
      if(q!=4096||lo[2]<6*q)throw std::runtime_error("unsupported scale or height");
      for(int i=0;i<3;++i)if(lo[i]<q||lo[i]>hi[i]||hi[i]>42*q)
        throw std::runtime_error("outside proved root");
      bool first=true;
      for(auto p:{std::array<int,3>{2,1,1},std::array<int,3>{1,2,1},std::array<int,3>{1,1,2}}) {
        I value=solve(q,lo,hi,p);
        if(value>q)throw std::runtime_error("finite predicate failed");
        if(!first)std::cout<<' ';
        first=false;std::cout<<value;
      }
      std::cout<<'\n';
      if(!std::cout)throw std::runtime_error("output failure");
    }
    if(!std::cin.eof())throw std::runtime_error("input read failure");
  }catch(const std::exception& error){std::cerr<<error.what()<<'\n';return 1;}
}
