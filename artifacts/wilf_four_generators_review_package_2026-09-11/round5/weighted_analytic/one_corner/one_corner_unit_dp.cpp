// Exact integer clipped-horn DP, specialized to unit weights.
// This is a fixed-height certificate, not a universal theorem by itself.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <vector>
using I=long long;
struct Result { I score; std::array<int,3> center; };
Result solve(int R, int penalty, std::array<int,3> p) {
  int n=R+1;
  auto idx=[n](int t,int b,int c){return (t*n+b)*n+c;};
  std::array<std::vector<I>,3> H;
  for(int axis=0;axis<3;axis++) {
    H[axis].assign((n+1)*n*n,0);
    int js[2],pos=0; for(int j=0;j<3;j++)if(j!=axis)js[pos++]=j;
    int pi=p[axis],pj=p[js[0]],pk=p[js[1]];
    auto &V=H[axis];
    for(int t=R;t>=0;t--)for(int b=0;b<=R;b++)for(int c=0;c<=R;c++) {
      I size=I(b+1)*(c+1),twosum=size*(2*t+b+c);
      int height=t+b+c;
      if(t>=pi&&b>=pj&&c>=pk) {
        I removed=I(b-pj+1)*(c-pk+1);
        size-=removed;twosum-=removed*(2*t+pj+b+pk+c);
        height=t+std::max(pj-1+c,b+pk-1);
      }
      I value=0;
      if(height<=R)value=std::max<I>(0,2*twosum+size*(penalty-3*R)+V[idx(t+1,b,c)]);
      if(b)value=std::max(value,V[idx(t,b-1,c)]);
      if(c)value=std::max(value,V[idx(t,b,c-1)]);
      V[idx(t,b,c)]=value;
    }
  }
  Result best{std::numeric_limits<I>::min(),{0,0,0}};
  for(int a=0;a<=R;a++)for(int b=0;b<=R;b++)for(int c=0;c<=R;c++) {
    I size=I(a+1)*(b+1)*(c+1),twosum=size*(a+b+c);int height=a+b+c;
    if(a>=p[0]&&b>=p[1]&&c>=p[2]) {
      I removed=I(a-p[0]+1)*(b-p[1]+1)*(c-p[2]+1);
      size-=removed;twosum-=removed*(a+p[0]+b+p[1]+c+p[2]);
      height=std::max({p[0]-1+b+c,a+p[1]-1+c,a+b+p[2]-1});
    }
    if(height>R)continue;
    I value=2*twosum+size*(penalty-3*R)+H[0][idx(a+1,b,c)]+H[1][idx(b+1,a,c)]+H[2][idx(c+1,a,b)];
    if(value>best.score)best={value,{a,b,c}};
  }
  return best;
}
int main(int argc,char**argv) {
  int first=argc>1?std::atoi(argv[1]):3,last=argc>2?std::atoi(argv[2]):8,penalty=argc>3?std::atoi(argv[3]):1;
  for(int R=first;R<=last;R++) {
    auto start=std::chrono::steady_clock::now();I score=std::numeric_limits<I>::min();int cases=0;std::array<int,3> pbest,center;
    for(int a=1;3*a<=R+1;a++)for(int b=a;a+2*b<=R+1;b++)for(int c=b;a+b+c<=R+1;c++) {
      auto r=solve(R,penalty,{a,b,c});cases++;
      if(r.score>score) {score=r.score;pbest={a,b,c};center=r.center;}
    }
    auto sec=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
    std::cout<<"{\"R\":"<<R<<",\"penalty\":"<<penalty<<",\"maximum\":"<<score<<",\"corner_cases\":"<<cases<<",\"corner\":["<<pbest[0]<<","<<pbest[1]<<","<<pbest[2]<<"],\"center\":["<<center[0]<<","<<center[1]<<","<<center[2]<<"],\"seconds\":"<<sec<<"}\n"<<std::flush;
  }
}
