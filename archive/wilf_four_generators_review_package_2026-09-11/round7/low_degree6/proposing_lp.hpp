#pragma once
#include <cmath>
#include <limits>
#include <numeric>
struct ProposingLP {
 int m,n;std::vector<int>B,N;std::vector<std::vector<double>>D;
 const double EPS=1e-8;
 ProposingLP(const std::vector<std::vector<double>>&A,const std::vector<double>&b,const std::vector<double>&c):m(b.size()),n(c.size()),B(m),N(n+1),D(m+2,std::vector<double>(n+2)){
  for(int i=0;i<m;i++)for(int j=0;j<n;j++)D[i][j]=A[i][j];
  for(int i=0;i<m;i++){B[i]=n+i;D[i][n]=-1;D[i][n+1]=b[i];}
  for(int j=0;j<n;j++){N[j]=j;D[m][j]=-c[j];}N[n]=-1;D[m+1][n]=1;
 }
 void pivot(int r,int s){
  double inv=1/D[r][s];
  for(int i=0;i<m+2;i++)if(i!=r)for(int j=0;j<n+2;j++)if(j!=s)D[i][j]-=D[r][j]*D[i][s]*inv;
  for(int j=0;j<n+2;j++)if(j!=s)D[r][j]*=inv;
  for(int i=0;i<m+2;i++)if(i!=r)D[i][s]*=-inv;
  D[r][s]=inv;std::swap(B[r],N[s]);
 }
 bool run(int phase){
  int row=phase==1?m+1:m;
  for(;;){
   int s=-1;
   for(int j=0;j<=n;j++)if(!(phase==2&&N[j]==-1))
    if(s==-1||D[row][j]<D[row][s]-EPS||(std::abs(D[row][j]-D[row][s])<=EPS&&N[j]<N[s]))s=j;
   if(D[row][s]>=-EPS)return true;
   int r=-1;
   for(int i=0;i<m;i++)if(D[i][s]>EPS)
    if(r==-1||D[i][n+1]/D[i][s]<D[r][n+1]/D[r][s]-EPS||(std::abs(D[i][n+1]/D[i][s]-D[r][n+1]/D[r][s])<=EPS&&B[i]<B[r]))r=i;
   if(r==-1)return false;pivot(r,s);
  }
 }
 bool solve(std::vector<double>&x){
  int r=0;for(int i=1;i<m;i++)if(D[i][n+1]<D[r][n+1])r=i;
  if(D[r][n+1]<-EPS){
   pivot(r,n);if(!run(1)||D[m+1][n+1]<-EPS||std::abs(D[m+1][n+1])>EPS)return false;
   for(int i=0;i<m;i++)if(B[i]==-1){int s=0;for(int j=1;j<=n;j++)if(D[i][j]<D[i][s]-EPS||(std::abs(D[i][j]-D[i][s])<=EPS&&N[j]<N[s]))s=j;pivot(i,s);}
  }
  if(!run(2))return false;x.assign(n,0);for(int i=0;i<m;i++)if(B[i]<n)x[B[i]]=D[i][n+1];return true;
 }
};
