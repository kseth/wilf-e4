#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <random>
#include <vector>

// Bounded falsification probe, NOT an exhaustive proof. Objective is the
// exact numerator 6 sum(Ap)-4 m max(Ap)-m*(a+b+c) for the cell-mean claim.
constexpr int INF=1000000000;
static void adjoin(std::vector<int>& d,int w) {
 int m=d.size(),step=w%m,g=std::gcd(m,step),L=m/g;
 for(int t=0;t<g;++t){int r=t;for(int k=0;k<2*L;++k){int n=r+step;if(n>=m)n-=m;d[n]=std::min(d[n],d[r]+w);r=n;}}
}
struct Result {bool valid=false, possible_interior=false;long long numerator=0,denominator=1,sum=0;int M=0;double score=-10;};
static Result evaluate(const std::array<int,4>& gs) {
 Result x;int m=gs[0]; if(!(m<gs[1]&&gs[1]<gs[2]&&gs[2]<gs[3]))return x;
 if(std::gcd(std::gcd(m,gs[1]),std::gcd(gs[2],gs[3]))!=1)return x;
 std::vector<int>d(m,INF);d[0]=0;
 for(int j=1;j<=3;++j){if(d[gs[j]%m]<=gs[j])return x;adjoin(d,gs[j]);}
 for(int v:d){x.sum+=v;x.M=std::max(x.M,v);}
 x.possible_interior = d[(m-gs[1]%m)%m]+gs[1] == d[(m-gs[2]%m)%m]+gs[2]
                   && d[(m-gs[1]%m)%m]+gs[1] == d[(m-gs[3]%m)%m]+gs[3];
 x.valid=true;long long s=gs[1]+gs[2]+gs[3];
 x.numerator=6*x.sum-4LL*m*x.M-m*s;
 x.denominator=1LL*m*(x.M+s);
 x.score=double(x.numerator)/x.denominator;return x;
}
int main(int argc,char**){
 bool interior_only=argc>1;
 std::mt19937_64 rng(74619243);std::array<int,4>bestgs{};Result best;long long attempts=0,valid=0;
 std::vector<int>ms={20,25,29,31,47,73,113,155,181,293,467,751,1213,1979,3181};
 for(int m:ms)for(int restart=0;restart<12;++restart){
   int scale=restart<4?2:restart<8?8:40;
   std::array<int,4>gs={m,m+1+int(rng()%(scale*m)),m+1+int(rng()%(scale*m)),m+1+int(rng()%(scale*m))};
   std::sort(gs.begin()+1,gs.end()); Result cur=evaluate(gs);
   if(interior_only&&!cur.possible_interior)cur.valid=false;
   for(int step=0;step<1800;++step){
     auto cand=gs;int j=1+rng()%3;int mode=rng()%6;int delta;
     if(mode==0)delta=1;else if(mode==1)delta=m;else if(mode==2)delta=1+rng()%m;else if(mode==3)delta=1+rng()%std::max(1,m/10);else if(mode==4)delta=1+rng()%(scale*m);else delta=1+rng()%std::max(1,m/40);
     if(rng()&1)delta=-delta;
     cand[j]=std::max(m+1,std::min(10000000,cand[j]+delta));std::sort(cand.begin()+1,cand.end());
     Result next=evaluate(cand);++attempts;if(!next.valid)continue;++valid;
     if(interior_only&&!next.possible_interior)continue;
     if(!best.valid||(__int128)next.numerator*best.denominator>(__int128)best.numerator*next.denominator){best=next;bestgs=cand;}
     double temp=.02*std::pow(.01,double(step)/1800.0);
     double uniform=double(rng()>>11)/9007199254740992.0;
     if(!cur.valid||next.score>=cur.score||uniform<std::exp((next.score-cur.score)/temp)){gs=cand;cur=next;}
   }
 }
 std::cout<<"{\"method\":\"targeted annealing diagnostic only\",\"interior_necessary_condition_required\":"<<(interior_only?"true":"false")<<",\"seed\":74619243,\"attempts\":"<<attempts<<",\"valid_candidates\":"<<valid<<",\"best_generators\":["<<bestgs[0]<<','<<bestgs[1]<<','<<bestgs[2]<<','<<bestgs[3]<<"],\"maximum_apery\":"<<best.M<<",\"sum_apery\":"<<best.sum<<",\"exact_failure_numerator\":"<<best.numerator<<",\"normalizing_denominator\":"<<best.denominator<<",\"positive_counterexample_found\":"<<(best.numerator>0?"true":"false")<<"}"<<std::endl;
}
