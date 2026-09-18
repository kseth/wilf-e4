// Independent exact interval worker, specialized disjoint-piece integration.
// Horn sections use TWO DISJOINT rectangles; centers use THREE DISJOINT boxes.
// No full-box-minus-excluded-box moments and no generating-worker source are used.
// The optimization recurrence is the separately audited nested-rectangle DP.
#include <algorithm>
#include <array>
#include <iostream>
#include <limits>
#include <vector>
using I=long long;
using V=std::array<I,3>;
struct Section { I count,twice_transverse,maximum_transverse; };
struct Horn { int B,C,stride;std::vector<I> data; };

// Rectangle [a,b] x [0,d], with no fixed outward coordinate.
// Twice its transverse moment is count*(w_j*(a+b)+w_k*d).
static inline Section rectangle(int a,int b,int d,I lj,I lk,I uj,I uk){
 if(a>b||d<0)return {0,0,0};
 I count=I(b-a+1)*(d+1);
 return {count,count*(uj*(a+b)+uk*d),lj*b+lk*d};
}
static inline Section section(int u,int v,int pj,int pk,I lj,I lk,I uj,I uk){
 if(u<pj||v<pk)return rectangle(0,u,v,lj,lk,uj,uk);
 // Disjoint union: [0,pj-1] x [0,v], [pj,u] x [0,pk-1].
 Section a=rectangle(0,pj-1,v,lj,lk,uj,uk);
 Section b=rectangle(pj,u,pk-1,lj,lk,uj,uk);
 return {a.count+b.count,a.twice_transverse+b.twice_transverse,
         std::max(a.maximum_transverse,b.maximum_transverse)};
}

static I solve(I scale,const V&lo,const V&hi,const std::array<int,3>&p){
 const V lower{scale,lo[0],lo[1]},upper{scale,hi[0],hi[1]};
 std::array<int,3> n;for(int i=0;i<3;i++)n[i]=hi[2]/lower[i]+1;
 const I offset=scale-3*lo[2];
 std::array<Horn,3> horn;
 for(int axis=0;axis<3;axis++){
  const int j=axis==0?1:0,k=axis==2?1:2;
  const int B=n[j],C=n[k],stride=B*C;auto &h=horn[axis];
  h.B=B;h.C=C;h.stride=stride;h.data.assign((n[axis]+1)*stride,0);
  // Two possible section profiles, before and after the outward corner cut.
  std::vector<Section> whole(stride),clipped(stride);
  for(int u=0;u<B;u++)for(int v=0;v<C;v++){
   int id=u*C+v;
   whole[id]=rectangle(0,u,v,lower[j],lower[k],upper[j],upper[k]);
   clipped[id]=section(u,v,p[j],p[k],lower[j],lower[k],upper[j],upper[k]);
  }
  for(int t=n[axis]-1;t>=0;t--){
   I*here=h.data.data()+t*stride;const I*later=here+stride;
   const auto &measure=t<p[axis]?whole:clipped;
   const I base=lower[axis]*t,coefficient=4*upper[axis]*t+offset;
   for(int u=0;u<B;u++){
    I row=0;
    for(int v=0;v<C;v++){
     int id=u*C+v;const auto &s=measure[id];
     if(base+s.maximum_transverse<=hi[2])
      row=std::max(row,s.count*coefficient+2*s.twice_transverse+later[id]);
     here[id]=std::max(row,u?here[id-C]:I(0));
    }
   }
  }
 }
 I best=std::numeric_limits<I>::min();
 for(int x=0;x<n[0];x++)for(int y=0;y<n[1];y++)for(int z=0;z<n[2];z++){
  I count=0,twice=0,maximum=0;
  if(x<p[0]||y<p[1]||z<p[2]){
   count=I(x+1)*(y+1)*(z+1);
   twice=count*(upper[0]*x+upper[1]*y+upper[2]*z);
   maximum=lower[0]*x+lower[1]*y+lower[2]*z;
  }else{
   // The first coordinate below the corner partitions the clipped center.
   // A: [0,px-1] x [0,y] x [0,z].
   I Na=I(p[0])*(y+1)*(z+1);
   I Sa=Na*(upper[0]*(p[0]-1)+upper[1]*y+upper[2]*z);
   I Ma=lower[0]*(p[0]-1)+lower[1]*y+lower[2]*z;
   // B: [px,x] x [0,py-1] x [0,z].
   I Nb=I(x-p[0]+1)*p[1]*(z+1);
   I Sb=Nb*(upper[0]*(p[0]+x)+upper[1]*(p[1]-1)+upper[2]*z);
   I Mb=lower[0]*x+lower[1]*(p[1]-1)+lower[2]*z;
   // C: [px,x] x [py,y] x [0,pz-1].
   I Nc=I(x-p[0]+1)*(y-p[1]+1)*p[2];
   I Sc=Nc*(upper[0]*(p[0]+x)+upper[1]*(p[1]+y)+upper[2]*(p[2]-1));
   I Mc=lower[0]*x+lower[1]*y+lower[2]*(p[2]-1);
   count=Na+Nb+Nc;twice=Sa+Sb+Sc;maximum=std::max({Ma,Mb,Mc});
  }
  if(maximum>hi[2])continue;
  I candidate=2*twice+count*offset;
  candidate+=horn[0].data[(x+1)*horn[0].stride+y*n[2]+z];
  candidate+=horn[1].data[(y+1)*horn[1].stride+x*n[2]+z];
  candidate+=horn[2].data[(z+1)*horn[2].stride+x*n[1]+y];
  best=std::max(best,candidate);
 }
 return best;
}
int main(){
 std::ios::sync_with_stdio(false);std::cin.tie(nullptr);
 I q;V lo,hi;
 while(std::cin>>q>>lo[0]>>lo[1]>>lo[2]>>hi[0]>>hi[1]>>hi[2]){
  V w{q,lo[0],lo[1]};I cap=hi[2]+q,best=std::numeric_limits<I>::min(),cases=0;
  std::array<int,3>chosen{0,0,0};
  // Full Cartesian corner enumeration, deliberately without symmetry pruning.
  for(int a=1;w[0]*a+w[1]+w[2]<=cap;a++)
   for(int b=1;w[0]*a+w[1]*b+w[2]<=cap;b++)
    for(int c=1;w[0]*a+w[1]*b+w[2]*c<=cap;c++){
     if(a+b+c<5)continue;
     std::array<int,3>p{a,b,c};I v=solve(q,lo,hi,p);cases++;
     if(v>best){best=v;chosen=p;}
    }
  std::cout<<best<<' '<<chosen[0]<<' '<<chosen[1]<<' '<<chosen[2]<<' '<<cases<<'\n'<<std::flush;
 }
}
