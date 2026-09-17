// Independent B5: subset profiles, literal column tops, explicit two-step moves.
#include <algorithm>
#include <array>
#include <bitset>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <vector>
using Integer=long long;
using Counter=unsigned long long;
struct Footprint { std::array<int,7> rows{}; int x=0,y=0; Counter code=0; };
static_assert(std::numeric_limits<Integer>::digits>=63,"value widths");
static_assert(std::numeric_limits<Counter>::digits>=64,"counter widths");
void verify(bool condition,const char* reason) { if(!condition)throw std::runtime_error(reason); }
bool qualifies(const Footprint& f,int x,int y,int degree) {
    if(f.rows[x]<=y)return false;
    int corners=0;
    for(int a=1;a<7;++a)for(int b=1;b<7;++b)
      corners+=(b>=f.rows[a] && b<f.rows[a-1] && b-1<f.rows[a]);
    return corners<=degree-2;
}
void checksum(Counter& c,Integer value) { c^=static_cast<Counter>(value); c*=1099511628211ULL; }
int main(int argc,char**) {
 try {
  verify(argc==1,"only full checking is supported");
  std::vector<Footprint> dictionary;
  for(unsigned subset=0;subset<(1u<<14);++subset) {
   if(std::bitset<14>(subset).count()!=7)continue;
   Footprint f;int at=0;bool degree_ok=true;
   for(int t=13;t>=0;--t)if(subset&(1u<<t)) {
    f.rows[at]=t-6+at;
    verify(f.rows[at]>=0&&f.rows[at]<=7,"subset conversion");
    degree_ok=degree_ok&&f.rows[at]<=7-at;++at;
   }
   if(!degree_ok||!f.rows[0])continue;
   f.y=f.rows[0];
   for(int i=0;i<7;++i) { f.x+=f.rows[i]>0;f.code+=Counter(f.rows[i])<<(3*i); }
   dictionary.push_back(f);
  }
  std::sort(dictionary.begin(),dictionary.end(),[](const Footprint&a,const Footprint&b){return a.rows<b.rows;});
  for(std::size_t i=1;i<dictionary.size();++i)verify(dictionary[i-1].rows!=dictionary[i].rows,"duplicate partition");
  std::vector<std::array<int,3>> corners;
  for(int P=5;P<=7;++P)for(int x=1;x<=P;++x)for(int y=x;y<=P;++y)
    if(P-x-y>=y)corners.push_back({x,y,P-x-y});
  Counter total=0;
  for(std::size_t pid=0;pid<corners.size();++pid) {
   auto p=corners[pid];int degree=p[0]+p[1]+p[2];
   std::array<std::vector<const Footprint*>,3> sections;
   for(const auto& f:dictionary) {
    if(qualifies(f,p[0],p[1],degree))sections[0].push_back(&f);
    if(qualifies(f,p[0],p[2],degree))sections[1].push_back(&f);
    if(qualifies(f,p[1],p[2],degree))sections[2].push_back(&f);
   }
   std::array<std::array<std::vector<const Footprint*>,8>,8> shared;
   for(auto h:sections[2])shared[h->x][h->y].push_back(h);
   Counter compatible=0,bounded=0,large=0,checked=0,local=0,axis_ok=0,fallback=0;
   Counter digest=14695981039346656037ULL; std::array<Counter,85> histogram{};
   Integer minimum=std::numeric_limits<Integer>::max(),minimum_den=1;
   for(auto f:sections[0])for(auto g:sections[1]) {
    if(f->x!=g->x)continue;
    for(auto h:shared[f->y][g->y]) {
     ++compatible;int height[9][9]{};Integer m=0,moments[3]={};bool bounded_degree=true;
     for(int x=0;x<f->x&&bounded_degree;++x)for(int y=0;y<f->rows[x];++y) {
      int length=std::min(g->rows[x],h->rows[y]);
      if(x>=p[0]&&y>=p[1])length=std::min(length,p[2]);
      verify(length>0,"empty compatible column");
      if(x+y+length-1>6) { bounded_degree=false;break; }
      height[x][y]=length;m+=length;moments[0]+=x*length;moments[1]+=y*length;
      moments[2]+=length*(length-1)/2;
     }
     if(!bounded_degree)continue;
     ++bounded;verify(m<=84,"degree-six cardinality");
     if(m<30)continue;++large;
     Integer intersections[3]={},gain=0,mass=0,weighted[3]={};
     for(int x=0;x<7;++x)for(int y=0;y<7;++y)for(int z=0;z<height[x][y];++z) {
      bool top[3]={z>=height[x+1][y],z>=height[x][y+1],z+1>=height[x][y]};
      intersections[0]+=top[0]&&top[1];intersections[1]+=top[0]&&top[2];intersections[2]+=top[1]&&top[2];
      bool one=!(top[0]&&top[1]&&top[2]);
      bool two=(z<height[x+2][y]||z<height[x][y+2]||z+2<height[x][y]||
                z<height[x+1][y+1]||z+1<height[x+1][y]||z+1<height[x][y+1]);
      verify(!two||one,"missing two-step predecessor");
      int coordinates[3]={x,y,z};
      for(int i=0;i<3;++i)if(top[i]) {
       int length=coordinates[i]+1;mass+=length;gain+=length*(two?2:one?1:0);
       for(int j=0;j<3;++j)weighted[j]+=length*coordinates[j];
      }
     }
     int extents[3]={f->x,f->y,g->y};
     if(intersections[0]>2*extents[2]||intersections[1]>2*extents[1]||intersections[2]>2*extents[0])continue;
     ++checked;++total;++histogram[m];
     verify(mass==3*m,"line mass");
     for(int j=0;j<3;++j)verify(weighted[j]==4*moments[j],"weighted tops");
     Integer q[3]={extents[0]-1,extents[1]-1,extents[2]-1};
     verify(q[0]>0&&q[1]>0&&q[2]>0,"axis positivity");
     Integer denominator=q[0]*q[1]*q[2],remainder=3*m*denominator;
     for(int i=0;i<3;++i)remainder-=4*moments[i]*(denominator/q[i]);
     Integer numerator=*std::max_element(q,q+3)*remainder;
     bool a=gain>=m,b=numerator>=m*denominator;
     verify(a||b,"no sufficient centroid witness");
     local+=a;axis_ok+=b;fallback+=!a;
     Integer margin=std::max(gain*denominator,numerator)-m*denominator;
     if(minimum==std::numeric_limits<Integer>::max()||margin*minimum_den<minimum*denominator) { minimum=margin;minimum_den=denominator; }
     for(Integer v:{Integer(f->code),Integer(g->code),Integer(h->code),m,moments[0],moments[1],moments[2],gain,numerator,denominator})checksum(digest,v);
    }
   }
   std::cout<<"{\"pid\":"<<pid<<",\"corner\":["<<p[0]<<","<<p[1]<<","<<p[2]
    <<"],\"compatible\":"<<compatible<<",\"degree_filtered\":"<<bounded<<",\"m30\":"<<large
    <<",\"eligible\":"<<checked<<",\"local_pass\":"<<local<<",\"axis_pass\":"<<axis_ok
    <<",\"axis_fallback\":"<<fallback<<",\"minimum_margin_numerator\":"<<minimum
    <<",\"minimum_margin_denominator\":"<<minimum_den<<",\"checksum\":"<<digest<<",\"histogram\":[";
   for(int i=0;i<85;++i) { if(i)std::cout<<",";std::cout<<histogram[i]; }
   std::cout<<"]}\n";std::cout.flush();
  }
  std::cout<<"{\"component\":\"B5-columns\",\"status\":\"PASS\",\"complete\":true,\"profiles\":"
           <<dictionary.size()<<",\"eligible\":"<<total<<"}\n";
  std::cout.flush();verify(bool(std::cout),"failed output");
 } catch(const std::exception& error) { std::cerr<<"B5 columns failed: "<<error.what()<<"\n";return 1; }
}
