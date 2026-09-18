// Independent complete replay: subset-generated planar profiles, explicit
// column-height arrays, direct surface/erosion counts, and a reverse dynamic program.
// Does not include any source/header or data file of the bitset producer.
// No LP, determinant, basis registry, or assignment stream is used.
#include <algorithm>
#include <array>
#include <cassert>
#include <cctype>
#include <climits>
#include <cstdint>
#include <fstream>
#include <iostream>
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
  uint64_t pure=0,axes=0,united=0,simple=0,simple_union=0;int minimum_upgrade=INT_MAX;I min_union_num=LLONG_MAX,min_union_den=1;int max_Q_excess=INT_MIN;
  std::array<uint64_t,85>hist{};
  int max_m=0,min_unit=INT_MAX;I min_num=LLONG_MAX,min_den=1;
};
int main(int argc,char**argv){
 try{
  const std::string dir=argc>1?argv[1]:"round10/ablation";
  const auto planes=make_planes();
  std::ofstream output(dir+"/independent_verification.jsonl");
  std::ofstream hard(dir+"/cheap_bound_exceptions_strong.jsonl");
  std::ofstream fallback(dir+"/axis_fallbacks_strong.jsonl");
  require(bool(output),"cannot write independent output");
  std::vector<std::array<int,3>> corners;
  for(int P=5;P<=7;++P)for(int x=1;x<=P;++x)for(int y=x;y<=P;++y){
    int z=P-x-y;if(z>=y)corners.push_back({x,y,z});
  }
  require(corners.size()==9,"corner enumeration");
  uint64_t total=0;
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
        if(e<=m)++count.erosion_ok; // Erosion recorded but not imposed.
        int Qxy=0,Qxz=0,Qyz=0,K=0;
        for(int x=0;x<7;++x)for(int y=0;y<7;++y){
          int h=H[x][y],hx=H[x+1][y],hy=H[x][y+1];
          Qxy+=std::max(0,h-std::max(hx,hy));
          Qxz+=h>hx;Qyz+=h>hy;K+=(h>hx&&h>hy);
        }
        int nx=0,ny=0,nz=H[0][0];
        for(int i=0;i<7;++i){nx+=H[i][0]>0;ny+=H[0][i]>0;}
        require(nx==a->nx&&ny==a->ny&&nz==b->ny,"axis agreement");
        if(Qxy>2*nz||Qxz>2*ny||Qyz>2*nx)continue;++count.q_ok;
        if(K<=6){++count.six_maxima;}
        ++count.remaining;++total;++count.hist[m];
        int D=3*m*R-4*(Sx+Sy+Sz);
        count.min_unit=std::min(count.min_unit,10*D-10*m+29);
        // Reverse dynamic program computes the largest degree above each point.
        // This differs from the producer's explicit scan of maximal points.
        int degree_above[8][8][8]{};
        int upgrade=0,top_mass=0,weighted_maxima=0;std::array<int,3> top_moment{};
        for(int x=6;x>=0;--x)for(int y=6;y>=0;--y)for(int z=6;z>=0;--z){
          if(z>=H[x][y])continue;
          int h=std::max({x+y+z,degree_above[x+1][y][z],degree_above[x][y+1][z],degree_above[x][y][z+1]});
          degree_above[x][y][z]=h;
          const bool top[3]={z>=H[x+1][y],z>=H[x][y+1],z+1>=H[x][y]};
          const int co[3]={x,y,z};
          if(top[0]&&top[1]&&top[2])weighted_maxima+=x+y+z+3;
          for(int i=0;i<3;++i)if(top[i]){
            int L=co[i]+1;top_mass+=L;
            for(int j=0;j<3;++j)top_moment[j]+=L*co[j];
            upgrade+=L*(h-x-y-z);
          }
        }
        require(top_mass==3*m,"coordinate-line mass identity");
        require(top_moment==std::array<int,3>{4*Sx,4*Sy,4*Sz},"coordinate-line moment identity");
        require(upgrade>=3*m-weighted_maxima,"universal simple line bound");
        int q0=nx-1,q1=ny-1,q2=nz-1;
        require(q0>0&&q1>0&&q2>0,"axis endpoint positive");
        int den=q0*q1*q2;
        int axis_numerator=std::max({q0,q1,q2})*(3*m*den-4*(Sx*q1*q2+Sy*q0*q2+Sz*q0*q1));
        bool pure=upgrade>=m,axes=axis_numerator>=m*den;
        bool simple=weighted_maxima<=2*m;
        count.pure+=pure;count.axes+=axes;count.united+=pure||axes;
        count.simple+=simple;count.simple_union+=simple||axes;
        count.minimum_upgrade=std::min(count.minimum_upgrade,upgrade-m);
        int un=std::max(upgrade*den,axis_numerator)-m*den;
        if(count.min_union_num==LLONG_MAX||un*count.min_union_den<count.min_union_num*den){count.min_union_num=un;count.min_union_den=den;}
        count.max_Q_excess=std::max(count.max_Q_excess,weighted_maxima-2*m);
        if(!pure){
          fallback<<"{\"corner\":["<<p[0]<<","<<p[1]<<","<<p[2]<<"],\"m\":"<<m<<",\"gain\":"<<upgrade<<",\"axis_numerator\":"<<axis_numerator<<",\"axis_denominator\":"<<den<<",\"profile_codes\":["<<a->code<<","<<b->code<<","<<c->code<<"],\"points\":[";
          bool f=true;for(int x=0;x<7;++x)for(int y=0;y<7;++y)for(int z=0;z<H[x][y];++z){if(!f)fallback<<",";f=false;fallback<<"["<<x<<","<<y<<","<<z<<"]";}fallback<<"]}\n";
        }
        if(!simple&&!axes){
          hard<<"{\"corner\":["<<p[0]<<","<<p[1]<<","<<p[2]<<"],\"m\":"<<m<<",\"gain\":"<<upgrade<<",\"weighted_maxima\":"<<weighted_maxima<<",\"axis_numerator\":"<<axis_numerator<<",\"axis_denominator\":"<<den<<",\"profile_codes\":["<<a->code<<","<<b->code<<","<<c->code<<"],\"points\":[";
          bool f=true;for(int x=0;x<7;++x)for(int y=0;y<7;++y)for(int z=0;z<H[x][y];++z){if(!f)hard<<",";f=false;hard<<"["<<x<<","<<y<<","<<z<<"]";}hard<<"]}\n";
        }
        require(pure||axes,"both closed-form centroid constructions failed");
        require(un>=0,"strong uniform centroid bound m failed");
      }
    }
    output<<"{\"pid\":"<<pid<<",\"corner\":["<<p[0]<<","<<p[1]<<","<<p[2]<<"]"
      <<",\"compatible\":"<<count.compatible<<",\"degree_ok\":"<<count.degree_ok
      <<",\"m30\":"<<count.m30<<",\"erosion_ok\":"<<count.erosion_ok<<",\"q_ok\":"<<count.q_ok
      <<",\"six_maxima\":"<<count.six_maxima<<",\"remaining\":"<<count.remaining
      <<",\"pure_upgrade\":"<<count.pure<<",\"axes\":"<<count.axes<<",\"union\":"<<count.united
      <<",\"simple_bound\":"<<count.simple<<",\"simple_or_axes\":"<<count.simple_union
      <<",\"minimum_gain_minus_m\":"<<count.minimum_upgrade
      <<",\"minimum_union_minus_m_numerator\":"<<count.min_union_num<<",\"minimum_union_minus_m_denominator\":"<<count.min_union_den
      <<",\"maximum_weighted_maxima_minus_2m\":"<<count.max_Q_excess
      <<",\"max_m_pre_erosion\":"<<count.max_m<<",\"smallest_tenth_margin\":"<<count.min_unit<<",\"histogram\":{";
    bool first=true;for(int m=30;m<85;++m)if(count.hist[m]){
      if(!first)output<<",";first=false;output<<"\""<<m<<"\":"<<count.hist[m];
    }
    output<<"}}\n";output.flush();
    std::cerr<<"pid "<<pid<<" verified "<<count.remaining<<" exact closed-form centroid checks; compatible "<<count.compatible<<"\n";
  }

  require(total==3909378,"unexpected total remaining shapes");
  std::cout<<"{\"status\":\"passed\",\"profiles\":"<<planes.size()
    <<",\"exact_closed_form_centroid_checks\":"<<total<<",\"floating_point_used\":false}\n";
 }catch(const std::exception&e){std::cerr<<"FAIL: "<<e.what()<<"\n";return 1;}
}
