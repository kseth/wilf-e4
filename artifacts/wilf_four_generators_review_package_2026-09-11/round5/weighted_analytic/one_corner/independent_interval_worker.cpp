// Independent interval DP audit: enumerate individual retained points for
// rectangle/box moments, and enumerate all rectangle choices explicitly.
// No clipped-box moment formula and no DP prefix-maximum shortcut are used.
#include <algorithm>
#include <array>
#include <iostream>
#include <limits>
#include <vector>
using I=long long;
struct A3 {
 int b,c; std::vector<I> v;
 A3(int a,int B,int C):b(B),c(C),v(a*B*C,0){}
 I& operator()(int i,int j,int k){return v[(i*b+j)*c+k];}
};
I solve(I q,std::array<I,3>lo,std::array<I,3>hi,std::array<int,3>p){
 std::array<I,3> lw={q,lo[0],lo[1]},uw={q,hi[0],hi[1]};
 std::array<int,3> n;for(int i=0;i<3;i++)n[i]=int(hi[2]/lw[i])+1;
 std::vector<A3> H;
 for(int i=0;i<3;i++){
  int js[2],k=0;for(int j=0;j<3;j++)if(j!=i)js[k++]=j;
  int B=n[js[0]],C=n[js[1]];
  H.emplace_back(n[i]+1,B,C);auto &h=H.back();
  for(int t=n[i]-1;t>=0;t--){
   int stride=C+1;std::vector<I> count((B+1)*stride,0),sum=count,mx=count;
   auto ix=[stride](int u,int v){return u*stride+v;};
   for(int u=0;u<B;u++)for(int v=0;v<C;v++){
    bool keep=!(t>=p[i]&&u>=p[js[0]]&&v>=p[js[1]]);
    I N=keep?1:0,S=keep?uw[i]*t+uw[js[0]]*u+uw[js[1]]*v:0,W=keep?lw[i]*t+lw[js[0]]*u+lw[js[1]]*v:0;
    count[ix(u+1,v+1)]=N+count[ix(u,v+1)]+count[ix(u+1,v)]-count[ix(u,v)];
    sum[ix(u+1,v+1)]=S+sum[ix(u,v+1)]+sum[ix(u+1,v)]-sum[ix(u,v)];
    mx[ix(u+1,v+1)]=std::max({W,mx[ix(u,v+1)],mx[ix(u+1,v)]});
   }
   for(int capu=0;capu<B;capu++)for(int capv=0;capv<C;capv++){
    I best=0;
    for(int u=0;u<=capu;u++)for(int v=0;v<=capv;v++){
     int z=ix(u+1,v+1);if(mx[z]>hi[2])continue;
     I value=4*sum[z]+count[z]*(q-3*lo[2])+h(t+1,u,v);
     best=std::max(best,value);
    }
    h(t,capu,capv)=best;
   }
  }
 }
 A3 cnt(n[0]+1,n[1]+1,n[2]+1),sum(n[0]+1,n[1]+1,n[2]+1),mx(n[0]+1,n[1]+1,n[2]+1);
 auto fill=[](A3&a,int i,int j,int k,I value){a(i+1,j+1,k+1)=value+a(i,j+1,k+1)+a(i+1,j,k+1)+a(i+1,j+1,k)-a(i,j,k+1)-a(i,j+1,k)-a(i+1,j,k)+a(i,j,k);};
 I best=std::numeric_limits<I>::min();
 for(int a=0;a<n[0];a++)for(int b=0;b<n[1];b++)for(int c=0;c<n[2];c++){
  bool keep=!(a>=p[0]&&b>=p[1]&&c>=p[2]);
  I N=keep?1:0,S=keep?uw[0]*a+uw[1]*b+uw[2]*c:0,W=keep?lw[0]*a+lw[1]*b+lw[2]*c:0;
  fill(cnt,a,b,c,N);fill(sum,a,b,c,S);
  mx(a+1,b+1,c+1)=std::max({W,mx(a,b+1,c+1),mx(a+1,b,c+1),mx(a+1,b+1,c)});
  if(mx(a+1,b+1,c+1)>hi[2])continue;
  I value=4*sum(a+1,b+1,c+1)+cnt(a+1,b+1,c+1)*(q-3*lo[2]);
  value+=H[0](a+1,b,c)+H[1](b+1,a,c)+H[2](c+1,a,b);
  best=std::max(best,value);
 }
 return best;
}
int main(){I q;std::array<I,3>lo,hi;
 while(std::cin>>q>>lo[0]>>lo[1]>>lo[2]>>hi[0]>>hi[1]>>hi[2]){
  bool first=true;for(auto p:{std::array<int,3>{2,1,1},std::array<int,3>{1,2,1},std::array<int,3>{1,1,2}}){if(!first)std::cout<<' ';first=false;std::cout<<solve(q,lo,hi,p);}std::cout<<'\n'<<std::flush;
 }
}
