#pragma once
#include <unordered_map>
#include <cassert>
struct ExactBasis {std::array<int,4> ids;std::array<std::array<long long,4>,4> adj;long long det;uint32_t serial;};
std::unordered_map<uint64_t,ExactBasis> basis_cache;
std::ofstream basis_output,assignment_output;
long long detmat(const std::vector<std::vector<long long>>&M){
 if(M.size()==1)return M[0][0];long long d=0;
 for(int j=0;j<(int)M.size();j++){
  std::vector<std::vector<long long>>sub;
  for(int i=1;i<(int)M.size();i++){std::vector<long long>r;for(int k=0;k<(int)M.size();k++)if(k!=j)r.push_back(M[i][k]);sub.push_back(r);}
  d+=(j%2?-1:1)*M[0][j]*detmat(sub);
 }
 return d;
}
std::array<long long,4> dualcol(int id){
 if(id<343)return {-id/49,-(id/7)%7,-id%7,1};
 std::array<long long,4>c{};if(id<347)c[id-343]=1;else c[3]=-1;return c;
}
const ExactBasis& basis(std::array<int,4>ids){
 std::sort(ids.begin(),ids.end());uint64_t key=0;for(int id:ids)key=key*512+id;
 auto got=basis_cache.find(key);if(got!=basis_cache.end())return got->second;
 std::vector<std::vector<long long>>M(4,std::vector<long long>(4));
 for(int j=0;j<4;j++){auto col=dualcol(ids[j]);for(int i=0;i<4;i++)M[i][j]=col[i];}
 ExactBasis b;b.ids=ids;b.det=detmat(M);assert(b.det);b.serial=basis_cache.size();
 for(int i=0;i<4;i++)for(int j=0;j<4;j++){
  std::vector<std::vector<long long>>sub;
  for(int r=0;r<4;r++)if(r!=j){std::vector<long long>v;for(int c=0;c<4;c++)if(c!=i)v.push_back(M[r][c]);sub.push_back(v);}
  b.adj[i][j]=((i+j)%2?-1:1)*detmat(sub);
 }
 if(b.det<0){b.det=-b.det;for(auto &row:b.adj)for(auto &v:row)v=-v;}
 basis_output<<"{\"id\":"<<b.serial<<",\"columns\":[";
 for(int i=0;i<4;i++)basis_output<<ids[i]<<(i==3?"]":" ,");
 basis_output<<",\"determinant\":"<<b.det<<"}\n";
 return basis_cache.emplace(key,b).first->second;
}
bool exact_dual(std::array<int,4>ids,int m,std::array<int,3>S,long long &margin_num,long long &denom){
 auto &b=basis(ids);std::array<long long,4>rhs={-4LL*S[0],-4LL*S[1],-4LL*S[2],3LL*m},v{},back{};long long bound=0;
 for(int i=0;i<4;i++)for(int j=0;j<4;j++)v[i]+=b.adj[i][j]*rhs[j];
 for(int i=0;i<4;i++){
  if(v[i]<0)return false;auto c=dualcol(b.ids[i]);
  for(int j=0;j<4;j++)back[j]+=c[j]*v[i];
  if(b.ids[i]>=343&&b.ids[i]<=345)bound+=v[i];if(b.ids[i]==347)bound-=7*v[i];
 }
 for(int j=0;j<4;j++)assert(back[j]==b.det*rhs[j]);
 margin_num=10*bound-(10LL*m-29)*b.det;denom=10*b.det;
 if(margin_num<0)return false;
 assignment_output.write(reinterpret_cast<const char*>(&b.serial),sizeof(b.serial));return true;
}
