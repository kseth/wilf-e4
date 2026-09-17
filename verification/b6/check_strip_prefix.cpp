// R6a A: subtractive box moments and monotone-prefix horn transitions.
#include <algorithm>
#include <array>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <vector>
using I=long long;
using P=std::array<int,3>;
static_assert(std::numeric_limits<I>::digits>=63,"signed scores");
static_assert(std::numeric_limits<int>::digits>=31,"indices");
void need(bool b,const char* reason){if(!b)throw std::runtime_error(reason);}
struct Stats{I count=0,twice=0;int maximum=0;};
Stats measure(P a,P b,const P&p){
 I count=1,twice_mean=0;int maximum=0;
 for(int i=0;i<3;++i){count*=b[i]-a[i]+1;twice_mean+=a[i]+b[i];maximum+=b[i];}
 Stats s{count,count*twice_mean,maximum};P cut;
 for(int i=0;i<3;++i){cut[i]=std::max(a[i],p[i]);if(cut[i]>b[i])return s;}
 I removed=1,removed_mean=0;
 for(int i=0;i<3;++i){removed*=b[i]-cut[i]+1;removed_mean+=cut[i]+b[i];}
 s.count-=removed;s.twice-=removed*removed_mean;s.maximum=0;
 for(int i=0;i<3;++i)if(a[i]<p[i]){
  int height=0;for(int j=0;j<3;++j)height+=i==j?std::min(b[j],p[j]-1):b[j];
  s.maximum=std::max(s.maximum,height);
 }
 need(s.count>0,"clipped center or section lost its axis");return s;
}
I solve(int R,const P&p){
 const int n=R+1;const I offset=4-3*R;
 auto id=[n](int t,int r,int s){return(t*n+r)*n+s;};
 std::array<std::vector<I>,3>horn;
 for(int i=0;i<3;++i){
  const int j=i==0?1:0,k=i==2?1:2;
  auto&H=horn[i];H.assign((n+1)*n*n,0);
  for(int t=R;t>=0;--t)for(int r=0;r<n;++r)for(int s=0;s<n;++s){
   P a{},b{};a[i]=b[i]=t;b[j]=r;b[k]=s;
   const auto q=measure(a,b,p);I value=0;
   if(q.maximum<=R)value=std::max<I>(0,2*q.twice+offset*q.count+H[id(t+1,r,s)]);
   if(r)value=std::max(value,H[id(t,r-1,s)]);
   if(s)value=std::max(value,H[id(t,r,s-1)]);
   H[id(t,r,s)]=value;
  }
 }
 bool found=false;I best=0;
 for(int x=0;x<n;++x)for(int y=0;y<n;++y)for(int z=0;z<n;++z){
  P c{x,y,z};const auto q=measure({0,0,0},c,p);if(q.maximum>R)continue;
  I value=2*q.twice+offset*q.count;
  value+=horn[0][id(x+1,y,z)]+horn[1][id(y+1,x,z)]+horn[2][id(z+1,x,y)];
  if(!found||value>best)best=value;found=true;
 }
 need(found,"no feasible center");return best;
}
int main(int argc,char**){
 try{
  need(argc==1,"only complete mode supported");int count=0;
  for(int R:{18,19,20,21})for(int a=1;3*a<=R+1;++a)
   for(int b=a;a+2*b<=R+1;++b)for(int c=b;a+b+c<=R+1;++c){
    P p{a,b,c};I v=solve(R,p);need(v<=0,"positive strip bound");
    std::cout<<R<<" "<<a<<" "<<b<<" "<<c<<" "<<v<<"\n";++count;
   }
  std::cout<<"PASS "<<count<<"\n";std::cout.flush();need(bool(std::cout),"output failure");
 }catch(const std::exception&e){std::cerr<<"R6a A failed: "<<e.what()<<"\n";return 1;}
}
