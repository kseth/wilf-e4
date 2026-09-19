// Finite Lemma 2.8: subtractive section moments and prefix-maxima horn DP.
#include <algorithm>
#include <array>
#include <iostream>
#include <limits>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
using I=long long;
static_assert(std::numeric_limits<I>::digits>=63,"signed values");
static_assert(std::numeric_limits<int>::digits>=31,"indices");
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
    // Compute retained section moments by subtracting the excluded upper rectangle.
    struct Profile {I count,twice_transverse,maximum_transverse;};
    std::vector<Profile> whole(nb*nc),clipped(nb*nc);
    for(int u=0;u<nb;u++)for(int v=0;v<nc;v++){
      I N=I(u+1)*(v+1);
      Profile s{N,N*(uw[other[0]]*u+uw[other[1]]*v),
                    lw[other[0]]*u+lw[other[1]]*v};
      whole[u*nc+v]=s;
      if(u>=p[other[0]]&&v>=p[other[1]]){
        I removed=I(u-p[other[0]]+1)*(v-p[other[1]]+1);
        s.count-=removed;
        s.twice_transverse-=removed*(uw[other[0]]*(p[other[0]]+u)
                                  +uw[other[1]]*(p[other[1]]+v));
        s.maximum_transverse=std::max(
          lw[other[0]]*(p[other[0]]-1)+lw[other[1]]*v,
          lw[other[0]]*u+lw[other[1]]*(p[other[1]]-1));
      }
      clipped[u*nc+v]=s;
    }
    for(int t=n[axis]-1;t>=0;t--){
      const auto &profile=t<p[axis]?whole:clipped;
      I base=lw[axis]*t,coefficient=4*uw[axis]*t+q-3*lo[2];
      for(int u=0;u<nb;u++)for(int v=0;v<nc;v++){
        const auto &s=profile[u*nc+v];
        I value=0;
        if(base+s.maximum_transverse<=hi[2])
          value=std::max<I>(0,s.count*coefficient+2*s.twice_transverse
                             +H[index(t+1,u,v)]);
        if(u)value=std::max(value,H[index(t,u-1,v)]);
        if(v)value=std::max(value,H[index(t,u,v-1)]);
        H[index(t,u,v)]=value;
      }
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
   if(q!=4096||lo[2]<7*q)throw std::runtime_error("unsupported scale or height");
   for(int i=0;i<3;++i)if(lo[i]<q||lo[i]>hi[i]||hi[i]>78*q)
    throw std::runtime_error("outside proved root");
   I cases=0,best=0;
   for(int P=5;P<=hi[2]/q+1;++P)for(int a=1;a<P-1;++a)for(int b=1;b<P-a;++b) {
    int c=P-a-b;if(q*a+lo[0]*b+lo[1]*c>hi[2]+q)continue;
    I value=solve(q,lo,hi,{a,b,c});
    if(!cases||value>best)best=value;
    ++cases;
   }
   if(cases&&10*best>29*q)throw std::runtime_error("high-height predicate failed");
   std::cout<<best<<" "<<cases<<"\n"<<std::flush;
   if(!std::cout)throw std::runtime_error("output failure");
  }
  if(!std::cin.eof())throw std::runtime_error("input read failure");
 }catch(const std::exception&e){std::cerr<<"high-height A failed: "<<e.what()<<"\n";return 1;}
}
