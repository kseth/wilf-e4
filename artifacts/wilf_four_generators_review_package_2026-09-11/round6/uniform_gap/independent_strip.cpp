// Separate exact checker: literal point scores, inclusive prefix sums,
// and all rectangle transitions. No rectangle moment formula or same-slice
// prefix maximum recurrence from the canonical program is used.
#include <algorithm>
#include <array>
#include <iostream>
#include <limits>
#include <vector>
using I=long long;

I independent(int R, std::array<int,3> p) {
  const int n=R+1;
  auto flat=[n](int t,int u,int v){return (t*n+u)*n+v;};
  auto keep=[p](const std::array<int,3>& x){return x[0]<p[0] || x[1]<p[1] || x[2]<p[2];};
  std::array<std::vector<I>,3> horn;
  for(int axis=0;axis<3;++axis) {
    auto& h=horn[axis]; h.assign((n+1)*n*n,0);
    std::array<int,2> js{}; int ix=0;
    for(int j=0;j<3;++j) if(j!=axis) js[ix++]=j;
    for(int t=R;t>=0;--t) {
      std::vector<I> sums(n*n,0);
      std::vector<int> heights(n*n,-1);
      for(int u=0;u<n;++u) for(int v=0;v<n;++v) {
        std::array<int,3> x{};x[axis]=t;x[js[0]]=u;x[js[1]]=v;
        const bool present=keep(x);
        I s=present ? 4*(t+u+v)+4-3*R : 0;
        int high=present ? t+u+v : -1;
        if(u) {s+=sums[(u-1)*n+v];high=std::max(high,heights[(u-1)*n+v]);}
        if(v) {s+=sums[u*n+v-1];high=std::max(high,heights[u*n+v-1]);}
        if(u&&v) s-=sums[(u-1)*n+v-1];
        sums[u*n+v]=s;heights[u*n+v]=high;
      }
      for(int b=0;b<n;++b) for(int c=0;c<n;++c) {
        I best=0;
        for(int u=0;u<=b;++u) for(int v=0;v<=c;++v)
          if(heights[u*n+v]<=R)
            best=std::max(best,sums[u*n+v]+h[flat(t+1,u,v)]);
        h[flat(t,b,c)]=best;
      }
    }
  }
  // Literal clipped central-box scores by a three-dimensional sum.
  std::vector<I> sums(n*n*n,0);
  std::vector<int> heights(n*n*n,-1);
  I best=std::numeric_limits<I>::min();
  for(int a=0;a<n;++a) for(int b=0;b<n;++b) for(int c=0;c<n;++c) {
    std::array<int,3> x{a,b,c};
    I s=keep(x) ? 4*(a+b+c)+4-3*R : 0;
    int high=keep(x) ? a+b+c : -1;
    for(int mask=1;mask<8;++mask) {
      int aa=a-(mask&1?1:0),bb=b-(mask&2?1:0),cc=c-(mask&4?1:0);
      if(aa<0||bb<0||cc<0) continue;
      int bits=(mask&1?1:0)+(mask&2?1:0)+(mask&4?1:0);
      s+=(bits%2?1:-1)*sums[flat(aa,bb,cc)];
      high=std::max(high,heights[flat(aa,bb,cc)]);
    }
    sums[flat(a,b,c)]=s;heights[flat(a,b,c)]=high;
    if(high<=R) best=std::max(best,s+horn[0][flat(a+1,b,c)]
      +horn[1][flat(b+1,a,c)]+horn[2][flat(c+1,a,b)]);
  }
  return best;
}
int main() {
  for(int R=18;R<=21;++R)
    for(int a=1;a<=R+1;++a)
      for(int b=a;b<=R+1;++b)
        for(int c=b;c<=R+1;++c)
          if(a+b+c<=R+1)
            std::cout<<R<<" "<<a<<" "<<b<<" "<<c<<" "<<independent(R,{a,b,c})<<"\n";
}
