// B5: recursive profiles; bitset surfaces and two-step successor masks.
#include <algorithm>
#include <array>
#include <bitset>
#include <cstdint>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <vector>
using I = long long;
using Count = unsigned long long;
using Row = std::array<int, 7>;
using Mask = std::bitset<343>;
static_assert(std::numeric_limits<I>::digits >= 63, "signed widths");
static_assert(std::numeric_limits<Count>::digits >= 64, "counter widths");
struct Plane { Row h{}; int nx=0, ny=0; Count code=0; };
void need(bool b, const char* message) { if (!b) throw std::runtime_error(message); }
void generate(Row& h, int i, int cap, std::vector<Plane>& pool) {
    if (i == 7) {
        Plane f; f.h=h; f.ny=h[0];
        for (int x=0;x<7;++x) { f.nx+=h[x]>0; f.code|=Count(h[x])<<(3*x); }
        if (f.ny) pool.push_back(f);
        return;
    }
    for (int v=0;v<=std::min(cap,7-i);++v) {
        h[i]=v; generate(h,i+1,v,pool);
    }
}
bool allowed(const Plane& f, int a, int b, int P) {
    if (f.h[a] <= b) return false;
    int drops=0;
    for (int x=1;x<f.nx;++x) drops+=f.h[x]<f.h[x-1];
    return drops<=P-2;
}
int index(int x,int y,int z) { return 49*x+7*y+z; }
void mix(Count& digest, I value) {
    // Defined unsigned modular checksum; never used to accept an ideal.
    digest=(digest ^ static_cast<Count>(value))*1099511628211ULL;
}
int main(int argc, char**) {
  try {
    need(argc==1,"partial modes unsupported");
    Row row{}; std::vector<Plane> pool; generate(row,0,7,pool);
    std::sort(pool.begin(),pool.end(),[](const Plane&a,const Plane&b){return a.h<b.h;});
    for (std::size_t i=1;i<pool.size();++i) need(pool[i-1].h!=pool[i].h,"duplicate profiles");
    std::array<Mask,3> interior;
    std::array<std::array<Mask,7>,3> levels;
    const int steps[3]={49,7,1};
    for(int x=0;x<7;++x)for(int y=0;y<7;++y)for(int z=0;z<7;++z) {
        int p[3]={x,y,z}, id=index(x,y,z);
        for(int i=0;i<3;++i) { levels[i][p[i]].set(id); if(p[i]<6)interior[i].set(id); }
    }
    const int corners[9][3]={{1,1,3},{1,2,2},{1,1,4},{1,2,3},{2,2,2},
                            {1,1,5},{1,2,4},{1,3,3},{2,2,3}};
    Count total=0;
    for(int pid=0;pid<9;++pid) {
      const auto& p=corners[pid]; int P=p[0]+p[1]+p[2];
      std::array<std::vector<const Plane*>,3> lists;
      for(const auto& f:pool) {
        if(allowed(f,p[0],p[1],P))lists[0].push_back(&f);
        if(allowed(f,p[0],p[2],P))lists[1].push_back(&f);
        if(allowed(f,p[1],p[2],P))lists[2].push_back(&f);
      }
      std::array<std::array<std::vector<const Plane*>,8>,8> group;
      for(auto h:lists[2])group[h->nx][h->ny].push_back(h);
      Count compatible=0,degree=0,m30=0,accepted=0,local=0,axes=0,fallback=0;
      Count digest=14695981039346656037ULL; std::array<Count,85> hist{};
      I min_num=std::numeric_limits<I>::max(),min_den=1;
      for(auto f:lists[0])for(auto g:lists[1]) {
        if(f->nx!=g->nx)continue;
        for(auto h:group[f->ny][g->ny]) {
          ++compatible; Mask T; std::vector<std::array<int,3>> points; I s[3]={};
          bool valid=true;
          for(int x=0;x<f->nx&&valid;++x)for(int y=0;y<f->h[x];++y) {
            int n=std::min(g->h[x],h->h[y]);
            if(x>=p[0]&&y>=p[1])n=std::min(n,p[2]);
            need(n>0,"shared axes lost a plane point");
            if(x+y+n-1>6) { valid=false; break; }
            for(int z=0;z<n;++z) { T.set(index(x,y,z)); points.push_back({x,y,z}); s[0]+=x;s[1]+=y;s[2]+=z; }
          }
          if(!valid)continue;
          ++degree; I m=points.size(); need(m<=84,"simplex size");
          if(m<30)continue; ++m30;
          std::array<Mask,3> top;
          Mask next;
          for(int i=0;i<3;++i) { Mask succ=(T>>steps[i])&interior[i]; top[i]=T&~succ; next|=succ; }
          const int n[3]={f->nx,f->ny,g->ny};
          if((top[0]&top[1]).count()>unsigned(2*n[2]) ||
             (top[0]&top[2]).count()>unsigned(2*n[1]) ||
             (top[1]&top[2]).count()>unsigned(2*n[0]))continue;
          ++accepted;++total;++hist[m];
          Mask twice;
          for(int i=0;i<3;++i)twice|=(next>>steps[i])&interior[i];
          I gain=0,mass=0; I top_moment[3]={};
          for(int i=0;i<3;++i)for(int t=0;t<7;++t) {
            Mask fibers=top[i]&levels[i][t];
            mass+=(t+1)*fibers.count();
            gain+=(t+1)*((fibers&next).count()+(fibers&twice).count());
          }
          for(const auto& q:points)for(int i=0;i<3;++i)if(top[i][index(q[0],q[1],q[2])])
            for(int j=0;j<3;++j)top_moment[j]+=(q[i]+1)*q[j];
          need(mass==3*m,"line mass");
          for(int j=0;j<3;++j)need(top_moment[j]==4*s[j],"line moment");
          I q0=n[0]-1,q1=n[1]-1,q2=n[2]-1;
          need(q0>0&&q1>0&&q2>0,"positive axes");
          I den=q0*q1*q2;
          I axis=std::max({q0,q1,q2})*(3*m*den-4*(s[0]*q1*q2+s[1]*q0*q2+s[2]*q0*q1));
          bool a=gain>=m,b=axis>=m*den; need(a||b,"both witnesses failed");
          local+=a;axes+=b;fallback+=!a;
          I num=std::max(gain*den,axis)-m*den;
          need(num>=0,"negative accepted margin");
          if(min_num==std::numeric_limits<I>::max() || num*min_den<min_num*den) { min_num=num;min_den=den; }
          for(I v:{I(f->code),I(g->code),I(h->code),m,s[0],s[1],s[2],gain,axis,den})mix(digest,v);
        }
      }
      std::cout<<"{\"pid\":"<<pid<<",\"corner\":["<<p[0]<<","<<p[1]<<","<<p[2]
       <<"],\"compatible\":"<<compatible<<",\"degree_filtered\":"<<degree
       <<",\"m30\":"<<m30<<",\"eligible\":"<<accepted<<",\"local_pass\":"<<local
       <<",\"axis_pass\":"<<axes<<",\"axis_fallback\":"<<fallback
       <<",\"minimum_margin_numerator\":"<<min_num<<",\"minimum_margin_denominator\":"<<min_den
       <<",\"checksum\":"<<digest<<",\"histogram\":[";
      for(int i=0;i<85;++i) { if(i)std::cout<<",";std::cout<<hist[i]; }
      std::cout<<"]}\n"; std::cout.flush();
    }
    need(bool(std::cout),"output failure");
    std::cout<<"{\"component\":\"B5-bitsets\",\"status\":\"PASS\",\"complete\":true,\"profiles\":"
             <<pool.size()<<",\"eligible\":"<<total<<"}\n";
    std::cout.flush();need(bool(std::cout),"summary output failure");
  } catch(const std::exception& e) { std::cerr<<"B5 bitsets failed: "<<e.what()<<"\n";return 1; }
}
