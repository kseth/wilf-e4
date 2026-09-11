// Independent complete replay: subset-generated planar profiles, explicit
// column-height arrays, direct surface/erosion counts, and Bareiss determinants.
// Does not include any source/header of the certificate producer.
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
using V=std::array<I,4>;
using M=std::array<V,4>;
struct Plane {std::array<int,7> h{};int nx=0,ny=0,code=0;};
struct Basis {std::array<int,4> ids{};M adj{};I det=0;};
void require(bool b,const std::string& msg){if(!b)throw std::runtime_error(msg);}
I determinant(M a){
  I sign=1,previous=1;
  for(int k=0;k<3;++k){
    int pivot=k;while(pivot<4&&a[pivot][k]==0)++pivot;
    if(pivot==4)return 0;
    if(pivot!=k){std::swap(a[pivot],a[k]);sign=-sign;}
    I current=a[k][k];
    for(int i=k+1;i<4;++i)for(int j=k+1;j<4;++j){
      __int128 numerator=(__int128)a[i][j]*current-(__int128)a[i][k]*a[k][j];
      require(numerator%previous==0,"nonintegral Bareiss step");
      numerator/=previous;
      require(numerator>=LLONG_MIN&&numerator<=LLONG_MAX,"determinant overflow");
      a[i][j]=(I)numerator;
    }
    for(int i=k+1;i<4;++i)a[i][k]=0;
    previous=current;
  }
  return sign*a[3][3];
}
V column(int id){
  require(id>=0&&id<=347,"column outside schema");
  if(id<343)return {-I(id/49),-I((id%49)/7),-I(id%7),1};
  V v{};if(id<=346)v[id-343]=1;else v[3]=-1;return v;
}
std::vector<I> integers(const std::string&s){
  std::vector<I> v;
  for(size_t i=0;i<s.size();){
    if(std::isdigit((unsigned char)s[i])||(s[i]=='-'&&i+1<s.size()&&std::isdigit((unsigned char)s[i+1]))){
      size_t j=i+1;while(j<s.size()&&std::isdigit((unsigned char)s[j]))++j;
      v.push_back(std::stoll(s.substr(i,j-i)));i=j;
    }else ++i;
  }return v;
}
std::vector<Basis> read_bases(const std::string& dir){
  std::ifstream f(dir+"/dual_bases.jsonl");require(bool(f),"missing basis registry");
  std::vector<Basis> bs;std::string line;
  while(std::getline(f,line)){
    auto z=integers(line);require(z.size()==6,"unexpected basis JSON schema");
    require(z[0]==(I)bs.size(),"basis ids not consecutive");
    Basis b;M a{};
    for(int j=0;j<4;++j){
      b.ids[j]=z[j+1];if(j)require(b.ids[j-1]<b.ids[j],"basis columns not strictly increasing");
      auto c=column(b.ids[j]);for(int i=0;i<4;++i)a[i][j]=c[i];
    }
    I d=determinant(a);require(d!=0,"singular basis");
    const I sign=d<0?-1:1;b.det=d*sign;
    require(b.det==z[5],"registry determinant mismatch");
    // Cramer's rule for each unit right-hand side; no cofactor formula.
    for(int j=0;j<4;++j)for(int i=0;i<4;++i){
      M replaced=a;for(int r=0;r<4;++r)replaced[r][j]=(r==i);
      b.adj[j][i]=sign*determinant(replaced);
    }
    for(int i=0;i<4;++i)for(int j=0;j<4;++j){
      I v=0;for(int k=0;k<4;++k)v+=a[i][k]*b.adj[k][j];
      require(v==(i==j?b.det:0),"basis inverse identity failure");
    }
    bs.push_back(b);
  }
  require(!bs.empty(),"empty basis registry");return bs;
}
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
  int max_m=0,min_unit=INT_MAX;I min_num=LLONG_MAX,min_den=1;
};
int main(int argc,char**argv){
 try{
  const std::string dir=argc>1?argv[1]:"round7/low_degree6";
  const auto bs=read_bases(dir);const auto planes=make_planes();
  std::ifstream assignments(dir+"/dual_assignments.bin",std::ios::binary);
  require(bool(assignments),"missing assignments");
  std::ofstream output(dir+"/independent_verification.jsonl");
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
        if(e>m)continue;++count.erosion_ok;
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
        if(K<=6){++count.six_maxima;continue;}
        ++count.remaining;++total;++count.hist[m];
        int D=3*m*R-4*(Sx+Sy+Sz);
        count.min_unit=std::min(count.min_unit,10*D-10*m+29);
        unsigned char bytes[4];assignments.read(reinterpret_cast<char*>(bytes),4);
        require(assignments.gcount()==4,"assignment stream ended early");
        uint32_t serial=uint32_t(bytes[0])|(uint32_t(bytes[1])<<8)|(uint32_t(bytes[2])<<16)|(uint32_t(bytes[3])<<24);
        require(serial<bs.size(),"assignment references missing basis");const auto&B=bs[serial];
        for(int id:B.ids)if(id<343){
          int x=id/49,y=(id%49)/7,z=id%7;
          require(z<H[x][y],"dual point constraint is absent from current ideal");
        }
        V rhs={-4LL*Sx,-4LL*Sy,-4LL*Sz,3LL*m},coef{},back{};
        for(int i=0;i<4;++i)for(int j=0;j<4;++j)coef[i]+=B.adj[i][j]*rhs[j];
        I bound=0;
        for(int j=0;j<4;++j){
          require(coef[j]>=0,"negative dual multiplier");
          auto col=column(B.ids[j]);for(int i=0;i<4;++i)back[i]+=col[i]*coef[j];
          if(B.ids[j]>=343&&B.ids[j]<=345)bound+=coef[j];
          if(B.ids[j]==347)bound-=7*coef[j];
        }
        for(int i=0;i<4;++i)require(back[i]==B.det*rhs[i],"dual equality failure");
        I margin=10*bound-(10LL*m-29)*B.det,den=10*B.det;
        require(margin>=0,"dual bound is below m-29/10");
        if(count.min_num==LLONG_MAX||(__int128)margin*count.min_den<(__int128)count.min_num*den){
          count.min_num=margin;count.min_den=den;
        }
      }
    }
    output<<"{\"pid\":"<<pid<<",\"corner\":["<<p[0]<<","<<p[1]<<","<<p[2]<<"]"
      <<",\"compatible\":"<<count.compatible<<",\"degree_ok\":"<<count.degree_ok
      <<",\"m30\":"<<count.m30<<",\"erosion_ok\":"<<count.erosion_ok<<",\"q_ok\":"<<count.q_ok
      <<",\"six_maxima\":"<<count.six_maxima<<",\"remaining\":"<<count.remaining
      <<",\"certificate_min_numerator\":"<<count.min_num<<",\"certificate_min_denominator\":"<<count.min_den
      <<",\"max_m_pre_erosion\":"<<count.max_m<<",\"smallest_tenth_margin\":"<<count.min_unit<<",\"histogram\":{";
    bool first=true;for(int m=30;m<85;++m)if(count.hist[m]){
      if(!first)output<<",";first=false;output<<"\""<<m<<"\":"<<count.hist[m];
    }
    output<<"}}\n";output.flush();
    std::cerr<<"pid "<<pid<<" verified "<<count.remaining<<" exact weighted duals; compatible "<<count.compatible<<"\n";
  }
  require(assignments.peek()==std::char_traits<char>::eof(),"extra assignment bytes remain");
  require(total==3361434,"unexpected total remaining shapes");
  std::cout<<"{\"status\":\"passed\",\"profiles\":"<<planes.size()<<",\"bases\":"<<bs.size()
    <<",\"exact_weighted_duals\":"<<total<<",\"floating_point_used\":false}\n";
 }catch(const std::exception&e){std::cerr<<"FAIL: "<<e.what()<<"\n";return 1;}
}
