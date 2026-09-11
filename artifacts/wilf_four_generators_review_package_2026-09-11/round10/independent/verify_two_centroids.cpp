// Independent scalar-height replay of two explicit centroid constructions.
// Planar enumeration and structural filters retained from the separate
// round9 replay; no producer source/header, bitset, LP registry or assignment.
#include <algorithm>
#include <array>
#include <climits>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <string>
#include <vector>
using I=long long;
struct Plane {std::array<int,7> h{};int nx=0,ny=0,code=0;};
void require(bool b,const std::string& msg){if(!b)throw std::runtime_error(msg);}
std::vector<Plane> make_planes(){
  std::vector<Plane> planes;
  // For each 7-subset t0>...>t6 of {0,...,13}, set hi=ti-6+i.
  // These are exactly the nonincreasing 7-row partitions in a 7x7 box.
  // Intersecting hi<=7-i imposes the degree-six planar simplex.
  for(unsigned bits=0;bits<(1u<<14);++bits){
    if(__builtin_popcount(bits)!=7)continue;
    Plane p;int i=0;bool valid=true;
    for(int t=13;t>=0;--t)if(bits&(1u<<t)){
      p.h[i]=t-6+i;require(p.h[i]>=0&&p.h[i]<=7,"partition conversion");
      if(p.h[i]>7-i)valid=false;++i;
    }
    if(!valid||p.h[0]==0)continue;
    p.ny=p.h[0];
    for(int x=0;x<7;++x){p.nx+=p.h[x]>0;p.code+=p.h[x]*(1<<(3*x));}
    planes.push_back(p);
  }
  std::sort(planes.begin(),planes.end(),[](const Plane&a,const Plane&b){return a.h<b.h;});
  for(size_t i=1;i<planes.size();++i)require(planes[i-1].h!=planes[i].h,"duplicate plane");
  require(planes.size()==1429,"wrong total planar profiles");return planes;
}
bool eligible(const Plane&p,int a,int b,int opp){
  if(p.h[a]<=b)return false;int mixed=0,upper=0;
  // Direct predecessor criterion for a planar mixed minimal exclusion.
  for(int x=1;x<7;++x)for(int y=1;y<7;++y){
    bool here=y<p.h[x],left=y<p.h[x-1],below=y-1<p.h[x];
    if(!here&&left&&below){++mixed;if(x>=a&&y>=b)++upper;}
  }
  return mixed<=a+b+opp-2&&upper<=opp;
}
struct Counts{
  uint64_t compatible=0,degree_ok=0,m30=0,erosion_ok=0,q_ok=0,six_maxima=0,remaining=0;
  std::array<uint64_t,85>hist{};
  int max_m=0,min_unit=INT_MAX,min_gain_margin=INT_MAX;
  uint64_t line=0,axis=0,union_count=0,cheap_line=0,cheap_union=0,line_m=0,axis_m=0,union_m=0;
  I min_combined_num=LLONG_MAX,min_combined_den=1,min_cheap_combined_num=LLONG_MAX,min_cheap_combined_den=1;
  I min_axis_fallback_num=LLONG_MAX,min_axis_fallback_den=1;
};
int main(int argc,char**argv){
 try{
  const std::string dir=argc>1?argv[1]:"round10/independent";
  const auto planes=make_planes();
  std::ofstream output(dir+"/coverage.jsonl"),exceptions(dir+"/line_exceptions.jsonl"),extrema(dir+"/successive_extrema.jsonl");
  require(bool(output)&&bool(exceptions),"cannot write output");
  std::vector<std::array<int,3>> corners;
  for(int P=5;P<=7;++P)for(int x=1;x<=P;++x)for(int y=x;y<=P;++y){
    int z=P-x-y;if(z>=y)corners.push_back({x,y,z});
  }
  require(corners.size()==9,"corner enumeration");
  uint64_t total=0,all_line=0,all_axis=0,all_union=0,all_cheap_union=0,strong_line=0,strong_axis=0,strong_union=0;
  for(int pid=0;pid<(int)corners.size();++pid){
    auto p=corners[pid];std::array<std::vector<const Plane*>,3> lists;
    for(const auto&q:planes){
      if(eligible(q,p[0],p[1],p[2]))lists[0].push_back(&q);
      if(eligible(q,p[0],p[2],p[1]))lists[1].push_back(&q);
      if(eligible(q,p[1],p[2],p[0]))lists[2].push_back(&q);
    }
    std::array<std::array<std::vector<const Plane*>,8>,8> group;
    for(auto q:lists[2])group[q->nx][q->ny].push_back(q);
    Counts count;
    for(auto a:lists[0])for(auto b:lists[1]){
      if(a->nx!=b->nx)continue;
      for(auto c:group[a->ny][b->ny]){
        ++count.compatible;
        int H[8][8]{};int m=0,R=0,Sx=0,Sy=0,Sz=0;bool degree=true;
        for(int x=0;x<a->nx&&degree;++x)for(int y=0;y<a->h[x];++y){
          int height=std::min(b->h[x],c->h[y]);
          if(x>=p[0]&&y>=p[1])height=std::min(height,p[2]);
          require(height>0,"compatible projections lost a plane point");
          if(x+y+height-1>6){degree=false;break;}
          H[x][y]=height;m+=height;R=std::max(R,x+y+height-1);
          Sx+=x*height;Sy+=y*height;Sz+=height*(height-1)/2;
        }
        if(!degree)continue;
        ++count.degree_ok;count.max_m=std::max(count.max_m,m);
        if(m<30)continue;++count.m30;
        int A[8][8]{};int e=0;
        for(int x=0;x<7;++x)for(int y=0;y<7;++y){
          A[x][y]=std::max(0,std::min({H[x][y]-1,H[x+1][y],H[x][y+1]}));
          e+=A[x][y]+(A[x][y]>0);
          if(x==0)e+=A[x][y];if(y==0)e+=A[x][y];
        }
        if(e>m)continue;++count.erosion_ok;
        int Qxy=0,Qxz=0,Qyz=0,K=0,maxima_degree_plus_three=0;
        for(int x=0;x<7;++x)for(int y=0;y<7;++y){
          int h=H[x][y],hx=H[x+1][y],hy=H[x][y+1];
          Qxy+=std::max(0,h-std::max(hx,hy));
          Qxz+=h>hx;Qyz+=h>hy;K+=(h>hx&&h>hy);
          if(h>hx&&h>hy)maxima_degree_plus_three+=x+y+h+2;
        }
        int nx=0,ny=0,nz=H[0][0];
        for(int i=0;i<7;++i){nx+=H[i][0]>0;ny+=H[0][i]>0;}
        require(nx==a->nx&&ny==a->ny&&nz==b->ny,"axis agreement");
        if(Qxy>2*nz||Qxz>2*ny||Qyz>2*nx)continue;++count.q_ok;
        if(K<=6){++count.six_maxima;}
        ++count.remaining;++total;++count.hist[m];
        int D=3*m*R-4*(Sx+Sy+Sz);
        count.min_unit=std::min(count.min_unit,10*D-10*m+29);
        // best[x][y][z] is the greatest degree of a point of T that
        // dominates (x,y,z). Scalar suffix recurrence, no maximal-point list.
        int best[8][8][8]{};
        for(int x=6;x>=0;--x)for(int y=6;y>=0;--y)for(int z=6;z>=0;--z){
          best[x][y][z]=std::max({z<H[x][y]?x+y+z:-100,
             best[x+1][y][z],best[x][y+1][z],best[x][y][z+1]});
        }
        int U=0;
        for(int x=0;x<7;++x)for(int y=0;y<7;++y)for(int z=0;z<H[x][y];++z){
          const int degree=x+y+z;
          if(z>=H[x+1][y]) U+=(x+1)*(best[x][y][z]-degree);
          if(z>=H[x][y+1]) U+=(y+1)*(best[x][y][z]-degree);
          if(z+1==H[x][y]) U+=(z+1)*(best[x][y][z]-degree);
        }
        const int qs[3]={nx-1,ny-1,nz-1};
        require(qs[0]>0&&qs[1]>0&&qs[2]>0,"axis length is zero");
        const I L=I(qs[0])*qs[1]*qs[2]; // product denominator, independent of producer lcm
        const I a_num=std::max({qs[0],qs[1],qs[2]})*(3LL*m*L-4LL*(Sx*(L/qs[0])+Sy*(L/qs[1])+Sz*(L/qs[2])));
        const I a_margin=10*a_num-(10LL*m-29)*L;
        const int cheap=3*m-maxima_degree_plus_three;
        require(U>=cheap,"cheap lower bound exceeded exact U");
        const bool line=U>=m-2,axis=a_margin>=0;
        const I combined_num=std::max(I(U)*L,a_num)-m*L;
        if(count.min_combined_num==LLONG_MAX||combined_num*count.min_combined_den<count.min_combined_num*L){
          count.min_combined_num=combined_num;count.min_combined_den=L;
          extrema<<"{\"pid\":"<<pid<<",\"m\":"<<m<<",\"profile_codes\":["<<a->code<<","<<b->code<<","<<c->code<<"],\"U\":"<<U
            <<",\"G_numerator\":"<<a_num<<",\"G_denominator\":"<<L<<",\"q\":["<<qs[0]<<","<<qs[1]<<","<<qs[2]<<"],\"s\":["<<Sx<<","<<Sy<<","<<Sz<<"],\"points\":[";
          bool fst=true;for(int x=0;x<7;++x)for(int y=0;y<7;++y)for(int z=0;z<H[x][y];++z){
            if(!fst)extrema<<",";fst=false;extrema<<"["<<x<<","<<y<<","<<z<<"]";
          }
          extrema<<"]}\n";
        }
        const I cheap_combined_num=std::max(I(cheap)*L,a_num)-m*L;
        if(count.min_cheap_combined_num==LLONG_MAX||cheap_combined_num*count.min_cheap_combined_den<count.min_cheap_combined_num*L){
          count.min_cheap_combined_num=cheap_combined_num;count.min_cheap_combined_den=L;
        }
        count.cheap_line+=cheap>=m-2;count.cheap_union+=(cheap>=m-2||axis);
        require(line||axis,"neither explicit centroid construction passed");
        require(U>=m||a_num>=m*L,"stronger D>=m bound failed");
        count.line_m+=U>=m;count.axis_m+=a_num>=m*L;++count.union_m;
        ++count.union_count;count.line+=line;count.axis+=axis;
        count.min_gain_margin=std::min(count.min_gain_margin,U-m+2);
        if(!line){
          if(count.min_axis_fallback_num==LLONG_MAX||(a_num-m*L)*count.min_axis_fallback_den<count.min_axis_fallback_num*L){
            count.min_axis_fallback_num=a_num-m*L;count.min_axis_fallback_den=L;
          }
          exceptions<<"{\"pid\":"<<pid<<",\"m\":"<<m<<",\"profile_codes\":["<<a->code<<","<<b->code<<","<<c->code<<"],\"U\":"<<U
           <<",\"axis_numerator\":"<<a_num<<",\"axis_denominator\":"<<L<<"}\n";
        }
      }
    }
    all_line+=count.line;all_axis+=count.axis;all_union+=count.union_count;all_cheap_union+=count.cheap_union;
    strong_line+=count.line_m;strong_axis+=count.axis_m;strong_union+=count.union_m;
    output<<"{\"pid\":"<<pid<<",\"corner\":["<<p[0]<<","<<p[1]<<","<<p[2]<<"]"
      <<",\"compatible\":"<<count.compatible<<",\"degree_ok\":"<<count.degree_ok
      <<",\"m30\":"<<count.m30<<",\"erosion_ok\":"<<count.erosion_ok<<",\"q_ok\":"<<count.q_ok
      <<",\"six_maxima\":"<<count.six_maxima<<",\"remaining\":"<<count.remaining
      <<",\"line_upgrade\":"<<count.line<<",\"axis_simplex\":"<<count.axis<<",\"union\":"<<count.union_count
      <<",\"line_at_least_m\":"<<count.line_m<<",\"axis_at_least_m\":"<<count.axis_m<<",\"union_at_least_m\":"<<count.union_m
      <<",\"cheap_line\":"<<count.cheap_line<<",\"cheap_union\":"<<count.cheap_union
      <<",\"min_combined_num\":"<<count.min_combined_num<<",\"min_combined_den\":"<<count.min_combined_den
      <<",\"min_cheap_combined_num\":"<<count.min_cheap_combined_num<<",\"min_cheap_combined_den\":"<<count.min_cheap_combined_den
      <<",\"min_gain_minus_m_plus_two\":"<<count.min_gain_margin
      <<",\"min_axis_fallback_G_minus_m_numerator\":"<<count.min_axis_fallback_num
      <<",\"min_axis_fallback_G_minus_m_denominator\":"<<count.min_axis_fallback_den
      <<",\"max_m_pre_erosion\":"<<count.max_m<<",\"smallest_tenth_margin\":"<<count.min_unit<<",\"histogram\":{";
    bool first=true;for(int m=30;m<85;++m)if(count.hist[m]){
      if(!first)output<<",";first=false;output<<"\""<<m<<"\":"<<count.hist[m];
    }
    output<<"}}\n";output.flush();
    std::cerr<<"pid "<<pid<<" verified "<<count.remaining<<" shapes; line "<<count.line<<" axis "<<count.axis<<"\n";
  }
  require(total==3742041,"unexpected total remaining shapes");
  require(all_line==3741920,"unexpected line coverage");
  require(all_union==total,"uncovered shapes");
  std::cout<<"{\"status\":\"passed\",\"profiles\":"<<planes.size()
    <<",\"shapes\":"<<total<<",\"line_upgrade\":"<<all_line<<",\"axis_simplex\":"<<all_axis
    <<",\"union\":"<<all_union<<",\"cheap_union\":"<<all_cheap_union
    <<",\"target\":\"D>=m\",\"line_at_least_m\":"<<strong_line<<",\"axis_at_least_m\":"<<strong_axis<<",\"union_at_least_m\":"<<strong_union<<",\"floating_point_used\":false,\"lp_certificates_used\":false}\n";
 }catch(const std::exception&e){std::cerr<<"FAIL: "<<e.what()<<"\n";return 1;}
}
