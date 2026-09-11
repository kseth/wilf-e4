// Independent clipped-horn certificate evaluator.
// Clipped boxes are integrated as disjoint boxes at the FIRST coordinate
// below the corner, rather than subtracting an upper box or using the
// generating worker's clipped-height formula.
#include <algorithm>
#include <array>
#include <iostream>
#include <limits>
#include <vector>
using I = long long;
using Vec = std::array<I,3>;
struct Measure { I count=0, twice=0, maximum=0; };

Measure integrate(const Vec& lower, const Vec& upper, const Vec& corner,
                  const Vec& feasible, const Vec& objective) {
    Measure result;
    for (int k=0;k<3;k++) {
        Vec lo=lower, hi=upper;
        for (int j=0;j<k;j++) lo[j]=std::max(lo[j],corner[j]);
        hi[k]=std::min(hi[k],corner[k]-1);
        I count=1, twice_weight=0, maximum=0;
        bool empty=false;
        for (int j=0;j<3;j++) {
            if (lo[j]>hi[j]) {empty=true;break;}
            count*=hi[j]-lo[j]+1;
            twice_weight+=objective[j]*(lo[j]+hi[j]);
            maximum+=feasible[j]*hi[j];
        }
        if (empty) continue;
        result.count+=count;
        result.twice+=count*twice_weight;
        result.maximum=std::max(result.maximum,maximum);
    }
    return result;
}

I evaluate(I scale,const Vec& lower,const Vec& upper,const Vec& p) {
    const Vec feasible{scale,lower[0],lower[1]}, objective{scale,upper[0],upper[1]};
    std::array<int,3> sizes;
    for(int j=0;j<3;j++) sizes[j]=upper[2]/feasible[j]+1;
    std::array<std::vector<std::vector<I>>,3> horn;
    for(int axis=0;axis<3;axis++) {
        int j=(axis==0?1:0), k=(axis==2?1:2);
        int nu=sizes[j],nv=sizes[k];
        horn[axis].assign(sizes[axis]+1,std::vector<I>(nu*nv,0));
        for(int t=sizes[axis]-1;t>=0;t--) {
            auto& here=horn[axis][t];const auto& later=horn[axis][t+1];
            for(int u=0;u<nu;u++) {
                I row_max=0;
                for(int v=0;v<nv;v++) {
                    Vec lo{0,0,0},hi{0,0,0};lo[axis]=hi[axis]=t;hi[j]=u;hi[k]=v;
                    Measure s=integrate(lo,hi,p,feasible,objective);
                    int index=u*nv+v;
                    if(s.maximum<=upper[2]) {
                        I candidate=2*s.twice+s.count*(scale-3*lower[2])+later[index];
                        row_max=std::max(row_max,candidate);
                    }
                    here[index]=std::max(row_max,u?here[index-nv]:I(0));
                }
            }
        }
    }
    I answer=std::numeric_limits<I>::min();
    for(int x=0;x<sizes[0];x++)for(int y=0;y<sizes[1];y++)for(int z=0;z<sizes[2];z++) {
        Vec top{x,y,z};Measure s=integrate({0,0,0},top,p,feasible,objective);
        if(s.maximum>upper[2])continue;
        I value=2*s.twice+s.count*(scale-3*lower[2]);
        for(int axis=0;axis<3;axis++) {
            int j=(axis==0?1:0),k=(axis==2?1:2);
            value+=horn[axis][top[axis]+1][top[j]*sizes[k]+top[k]];
        }
        answer=std::max(answer,value);
    }
    return answer;
}

int main() {
    std::ios::sync_with_stdio(false);std::cin.tie(nullptr);
    I scale;Vec lo,hi;
    while(std::cin>>scale>>lo[0]>>lo[1]>>lo[2]>>hi[0]>>hi[1]>>hi[2]) {
        std::cout<<evaluate(scale,lo,hi,{2,1,1})<<' '
                 <<evaluate(scale,lo,hi,{1,2,1})<<' '
                 <<evaluate(scale,lo,hi,{1,1,2})<<'\n';
    }
}
