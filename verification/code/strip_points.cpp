// Finite Lemma 2.7: literal-point section prefixes and direct rectangle transitions.
#include <algorithm>
#include <array>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <vector>
using Value=long long;
using Triple=std::array<int,3>;
static_assert(std::numeric_limits<Value>::digits>=63,"values");
static_assert(std::numeric_limits<int>::digits>=31,"indices");
void check(bool b,const char*why){if(!b)throw std::runtime_error(why);}
Value evaluate(int R,const Triple&corner){
 int n=R+1,m=n+1;
 auto address=[n](int t,int u,int v){return(t*n+u)*n+v;};
 auto cube=[m](int a,int b,int c){return(a*m+b)*m+c;};
 std::vector<Value>scores(m*m*m,0);
 std::vector<int>heights(m*m*m,0);
 // Inclusive central prefixes from actual retained points.
 for(int x=0;x<n;++x)for(int y=0;y<n;++y)for(int z=0;z<n;++z){
  bool retained=x<corner[0]||y<corner[1]||z<corner[2];
  Value point=retained?4*(x+y+z)+4-3*R:0;
  int a=x+1,b=y+1,c=z+1;
  scores[cube(a,b,c)]=point+scores[cube(a-1,b,c)]+scores[cube(a,b-1,c)]
   +scores[cube(a,b,c-1)]-scores[cube(a-1,b-1,c)]-scores[cube(a-1,b,c-1)]
   -scores[cube(a,b-1,c-1)]+scores[cube(a-1,b-1,c-1)];
  heights[cube(a,b,c)]=std::max({retained?x+y+z:0,heights[cube(a-1,b,c)],
                                heights[cube(a,b-1,c)],heights[cube(a,b,c-1)]});
 }
 std::array<std::vector<Value>,3>parts;
 for(int axis=0;axis<3;++axis){
  int j=axis==0?1:0,k=axis==2?1:2;auto&dp=parts[axis];
  dp.assign((n+1)*n*n,0);
  for(int t=R;t>=0;--t){
   std::vector<Value>section(m*m,0),candidate(n*n,0);
   std::vector<int>degree(m*m,0);
   for(int u=0;u<n;++u)for(int v=0;v<n;++v){
    Triple point{};point[axis]=t;point[j]=u;point[k]=v;
    bool keep=point[0]<corner[0]||point[1]<corner[1]||point[2]<corner[2];
    int a=u+1,b=v+1;
    section[a*m+b]=(keep?4*(t+u+v)+4-3*R:0)
     +section[(a-1)*m+b]+section[a*m+b-1]-section[(a-1)*m+b-1];
    degree[a*m+b]=std::max({keep?t+u+v:0,degree[(a-1)*m+b],degree[a*m+b-1]});
    if(degree[a*m+b]<=R)candidate[u*n+v]=section[a*m+b]+dp[address(t+1,u,v)];
   }
   for(int U=0;U<n;++U)for(int V=0;V<n;++V){
    Value best=0;
    for(int u=0;u<=U;++u)for(int v=0;v<=V;++v)best=std::max(best,candidate[u*n+v]);
    dp[address(t,U,V)]=best;
   }
  }
 }
 bool exists=false;Value answer=0;
 for(int x=0;x<n;++x)for(int y=0;y<n;++y)for(int z=0;z<n;++z){
  int index=cube(x+1,y+1,z+1);if(heights[index]>R)continue;
  Value value=scores[index]+parts[0][address(x+1,y,z)]
   +parts[1][address(y+1,x,z)]+parts[2][address(z+1,x,y)];
  if(!exists||value>answer)answer=value;exists=true;
 }
 check(exists,"empty central search");return answer;
}
int main(int argc,char**){
 try{
  check(argc==1,"partial or unsupported mode");int total=0;
  for(int R=18;R<=20;++R){
   std::vector<Triple>configurations;
   for(int x=1;x<=R;++x)for(int y=1;y<=R;++y)for(int z=1;z<=R;++z)
    if(x<=y&&y<=z&&x+y+z<=R+1)configurations.push_back({x,y,z});
   for(auto p:configurations){
    Value bound=evaluate(R,p);check(bound<=0,"strip predicate failed");
    std::cout<<R<<" "<<p[0]<<" "<<p[1]<<" "<<p[2]<<" "<<bound<<"\n";++total;
   }
  }
  std::cout<<"PASS "<<total<<"\n";std::cout.flush();check(bool(std::cout),"output error");
 }catch(const std::exception&e){std::cerr<<"strip B failed: "<<e.what()<<"\n";return 1;}
}
