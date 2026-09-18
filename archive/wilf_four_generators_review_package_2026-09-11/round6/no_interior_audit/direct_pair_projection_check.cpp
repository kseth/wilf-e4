// Independent finite diagnostic: construct every pair-determined lower ideal
// with all three axis maxima equal to 4, then search directly for a valid
// central box and three rectangular outward horns. No clique-tree or DP code.
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <vector>
using P=std::array<int,3>;
constexpr int L=4;
using Row=std::array<int,L+1>;
std::vector<Row> rows;
void make_rows(Row r,int i,int hi){
  if(i>L){rows.push_back(r);return;}
  for(int n=0;n<=hi;n++){r[i]=n;make_rows(r,i+1,n);}
}
bool member(const P& p,const Row& xy,const Row& xz,const Row& yz){
  if(*std::max_element(p.begin(),p.end())>L)return false;
  return p[1]<=xy[p[0]]&&p[2]<=xz[p[0]]&&p[2]<=yz[p[1]];
}
bool center_works(const std::vector<P>& T,const P& a){
  for(const auto&p:T){int excess=0;for(int i=0;i<3;i++)excess+=(p[i]>a[i]);if(excess>1)return false;}
  for(int axis=0;axis<3;axis++)for(int t=a[axis]+1;t<=L;t++){
    int j=(axis+1)%3,k=(axis+2)%3,maxj=-1,maxk=-1,count=0;
    for(const auto&p:T)if(p[axis]==t){++count;maxj=std::max(maxj,p[j]);maxk=std::max(maxk,p[k]);}
    if(count!=(maxj+1)*(maxk+1)||maxj>a[j]||maxk>a[k])return false;
  }
  return true;
}
int main(){Row seed{};seed[0]=L;make_rows(seed,1,L);long long tested=0;int max_size=0,max_maxima=0;
  for(const auto&xy:rows)for(const auto&xz:rows)for(const auto&yz:rows){
    std::vector<P>T, maxima;
    for(int x=0;x<=L;x++)for(int y=0;y<=L;y++)for(int z=0;z<=L;z++){
      P p{x,y,z};if(member(p,xy,xz,yz))T.push_back(p);
    }
    for(const auto&p:T){bool maximal=true;for(int i=0;i<3;i++){auto q=p;++q[i];if(member(q,xy,xz,yz)){maximal=false;break;}}if(maximal)maxima.push_back(p);}
    bool found=false;for(const auto&a:maxima)if(center_works(T,a)){found=true;break;}
    if(!found){std::cerr<<"Failure for pair arrays\n";for(auto r:{xy,xz,yz}){for(auto v:r)std::cerr<<v<<' ';std::cerr<<'\n';}return 1;}
    ++tested;max_size=std::max(max_size,(int)T.size());max_maxima=std::max(max_maxima,(int)maxima.size());
  }
  std::cout<<"{\"axis_maximum\":"<<L<<",\"pair_arrays\":"<<rows.size()<<",\"tested\":"<<tested<<",\"maximum_size\":"<<max_size<<",\"maximum_maximal_points\":"<<max_maxima<<",\"failures\":0,\"scope\":\"finite diagnostic, not the proof\"}\n";
}
