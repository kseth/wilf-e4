#include <array>
#include <iostream>
#include <vector>
using namespace std;
int main(){
 int count;cin>>count;
 cout<<"[";bool first=true;
 for(int idx=0;idx<count;idx++){
  int m;cin>>m;
  if(m<1 || m>64){cerr<<"This checker requires 1 <= m <= 64.\n";return 2;}
  vector<array<int,3>> t(m);
  for(auto &x:t)cin>>x[0]>>x[1]>>x[2];
  for(int a=1;a<m;a++)for(int b=1;b<m;b++)if(b!=a)for(int c=1;c<m;c++)if(c!=a && c!=b){
   unsigned long long seen=0;bool ok=true;
   for(auto x:t){int r=(a*x[0]+b*x[1]+c*x[2])%m;auto bit=1ULL<<r;if(seen&bit){ok=false;break;}seen|=bit;}
   if(ok){if(!first)cout<<",";first=false;cout<<"["<<idx<<","<<a<<","<<b<<","<<c<<"]";}
  }
 }
 cout<<"]\n";
}
