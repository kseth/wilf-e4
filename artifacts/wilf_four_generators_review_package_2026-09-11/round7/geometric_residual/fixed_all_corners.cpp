// Exact interval horn DP worker. All mathematical arithmetic is signed 64-bit.
// Fixed-parameter diagnostic over all positive corners.
// Input: q B C M. Output echoes parameters then maximum, corner, and count.
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
 I q,B,C,M;while(std::cin>>q>>B>>C>>M){
 std::array<I,3>lo={B,C,M},hi=lo;
 I best=std::numeric_limits<I>::min();std::array<int,3>bp;long long count=0;
 for(int a=1;q*a+B+C<=M+q;a++)for(int b=1;q*a+B*b+C<=M+q;b++)for(int c=1;q*a+B*b+C*c<=M+q;c++){
 if(q==B && a>b)continue;if(B==C&&b>c)continue;
 std::array<int,3>p={a,b,c};I v=solve(q,lo,hi,p);count++;
 if(v>best){best=v;bp=p;}
 }
 std::cout<<q<<" "<<B<<" "<<C<<" "<<M<<" "<<best<<" "<<bp[0]<<" "<<bp[1]<<" "<<bp[2]<<" "<<count<<std::endl;
 }
}
