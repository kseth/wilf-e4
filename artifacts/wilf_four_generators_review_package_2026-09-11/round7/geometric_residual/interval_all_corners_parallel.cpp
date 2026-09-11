#include <atomic>
#include <omp.h>
// Exact interval horn DP worker. All mathematical arithmetic is signed 64-bit.
// Generic full-support corners of coordinate sum at least five.
// Interval input: q B0 C0 H0 B1 C1 H1.
// Interval output: bound, maximizing corner coordinates, count, completion flag.
#include <algorithm>
#include <array>
#include <iostream>
#include <limits>
#include <vector>
using I=long long;

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
    for(int t=n[axis]-1;t>=0;t--)for(int u=0;u<nb;u++)for(int v=0;v<nc;v++){
      I count=I(u+1)*(v+1);
      I height=lw[axis]*t+lw[other[0]]*u+lw[other[1]]*v;
      I twice=count*(2*uw[axis]*t+uw[other[0]]*u+uw[other[1]]*v);
      if(t>=p[axis]&&u>=p[other[0]]&&v>=p[other[1]]){
        I removed=I(u-p[other[0]]+1)*(v-p[other[1]]+1);count-=removed;
        twice-=removed*(2*uw[axis]*t+uw[other[0]]*(p[other[0]]+u)+uw[other[1]]*(p[other[1]]+v));
        height=lw[axis]*t+std::max(lw[other[0]]*(p[other[0]]-1)+lw[other[1]]*v,lw[other[0]]*u+lw[other[1]]*(p[other[1]]-1));
      }
      I value=0;
      if(height<=hi[2])value=std::max<I>(0,2*twice+count*(q-3*lo[2])+H[index(t+1,u,v)]);
      if(u)value=std::max(value,H[index(t,u-1,v)]);
      if(v)value=std::max(value,H[index(t,u,v-1)]);
      H[index(t,u,v)]=value;
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




int main(){
 omp_set_num_threads(4);
 I q;std::array<I,3>lo,hi;
 while(std::cin>>q>>lo[0]>>lo[1]>>lo[2]>>hi[0]>>hi[1]>>hi[2]){
 I best=std::numeric_limits<I>::min();std::array<int,3>bp={0,0,0};long long count=0;std::atomic<bool>stopped(false);
 std::vector<std::array<int,3>> points;
 for(int P=5;P<=int(hi[2]/q)+1;P++)for(int a=1;a<=P-2;a++)for(int b=1;b<=P-a-1;b++){
 int c=P-a-b;if(q*a+lo[0]*b+lo[1]*c>hi[2]+q)continue;
 if(q==lo[0]&&q==hi[0]&&a>b)continue;
 if(lo[0]==lo[1]&&hi[0]==hi[1]&&b>c)continue;
 points.push_back({a,b,c});
 }
 int first=std::min<int>(points.size(),20);
 for(int i=0;i<first&&!stopped.load();i++){
 auto p=points[i];I v=solve(q,lo,hi,p);count++;
 if(v>best){best=v;bp=p;}if(10*v>29*q)stopped.store(true);
 }
 if(!stopped.load()){
 #pragma omp parallel for schedule(dynamic,8) if(points.size()>200)
 for(int i=first;i<int(points.size());i++){
 if(stopped.load())continue;
 auto p=points[i];I v=solve(q,lo,hi,p);
 #pragma omp critical
 {count++;if(v>best){best=v;bp=p;}if(10*v>29*q)stopped.store(true);}
 }
 }
 std::cout<<best<<" "<<bp[0]<<" "<<bp[1]<<" "<<bp[2]<<" "<<count<<" "<<int(!stopped.load())<<std::endl;
 }
}
