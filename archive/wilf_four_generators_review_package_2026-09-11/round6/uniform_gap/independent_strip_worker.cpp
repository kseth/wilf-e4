// Independent unit-weight clipped-horn evaluator.
// Uses disjoint clipped-box integration and explicit rectangle transitions.
#include <algorithm>
#include <array>
#include <chrono>
#include <iostream>
#include <limits>
#include <vector>
using Integer = long long;
using Triple = std::array<int,3>;
struct Integral { Integer count=0, twice_moment=0; int height=0; };

Integral measure(Triple low, Triple high, const Triple& corner) {
    Integral ans;
    // Each retained point is assigned to its first coordinate below corner.
    for (int first=0; first<3; ++first) {
        Triple lo=low, hi=high;
        for (int i=0; i<first; ++i) lo[i]=std::max(lo[i],corner[i]);
        hi[first]=std::min(hi[first],corner[first]-1);
        Integer count=1;
        int sum_endpoints=0, height=0;
        for (int i=0;i<3;++i) {
            if (lo[i]>hi[i]) { count=0; break; }
            count*=hi[i]-lo[i]+1;
            sum_endpoints+=lo[i]+hi[i];
            height+=hi[i];
        }
        if (!count) continue;
        ans.count+=count;
        ans.twice_moment+=count*sum_endpoints;
        ans.height=std::max(ans.height,height);
    }
    return ans;
}

Integer solve(int radius,int penalty, const Triple& corner) {
    const int n=radius+1;
    const Integer impossible=std::numeric_limits<Integer>::lowest()/4;
    std::array<std::vector<Integer>,3> arms;
    auto index=[n](int t,int u,int v) { return (t*n+u)*n+v; };
    for (int axis=0;axis<3;++axis) {
        const int j=axis==0?1:0, k=axis==2?1:2;
        arms[axis].assign((n+1)*n*n,0);
        std::vector<Integer> candidate(n*n);
        for (int t=radius;t>=0;--t) {
            for (int u=0;u<n;++u) for (int v=0;v<n;++v) {
                Triple lo{0,0,0},hi{0,0,0};
                lo[axis]=hi[axis]=t; hi[j]=u; hi[k]=v;
                Integral s=measure(lo,hi,corner);
                candidate[u*n+v]=s.height>radius?impossible:
                    2*s.twice_moment+(penalty-3*radius)*s.count
                    +arms[axis][index(t+1,u,v)];
            }
            // Deliberately no prefix-max identity: enumerate every allowed
            // transverse rectangle for each independent state of the arm.
            for (int umax=0;umax<n;++umax) for (int vmax=0;vmax<n;++vmax) {
                Integer best=0;
                for (int u=0;u<=umax;++u) for (int v=0;v<=vmax;++v)
                    best=std::max(best,candidate[u*n+v]);
                arms[axis][index(t,umax,vmax)]=best;
            }
        }
    }
    Integer best=impossible;
    for (int x=0;x<n;++x) for (int y=0;y<n;++y) for (int z=0;z<n;++z) {
        Integral s=measure({0,0,0},{x,y,z},corner);
        if (s.height>radius) continue;
        Integer candidate=2*s.twice_moment+(penalty-3*radius)*s.count;
        candidate+=arms[0][index(x+1,y,z)];
        candidate+=arms[1][index(y+1,x,z)];
        candidate+=arms[2][index(z+1,x,y)];
        best=std::max(best,candidate);
    }
    return best;
}

int main(int argc,char**argv) {
    const int lower=argc>1?std::stoi(argv[1]):18;
    const int upper=argc>2?std::stoi(argv[2]):21;
    const int penalty=argc>3?std::stoi(argv[3]):4;
    for (int r=lower;r<=upper;++r) {
        auto started=std::chrono::steady_clock::now();
        Integer maximum=std::numeric_limits<Integer>::lowest();
        int count=0;
        for (int x=1;x<=r;++x) for (int y=1;y<=r;++y) for (int z=1;z<=r;++z) {
            if (x>y || y>z || x+y+z>r+1) continue;
            Integer score=solve(r,penalty,{x,y,z});
            std::cout << "{\"R\":" << r << ",\"penalty\":" << penalty
                      << ",\"corner\":["<<x<<','<<y<<','<<z<<"],\"maximum\":"<<score<<"}\n";
            maximum=std::max(maximum,score); ++count;
        }
        double seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-started).count();
        std::cerr << "{\"R\":"<<r<<",\"penalty\":"<<penalty
                  <<",\"corner_cases\":"<<count<<",\"maximum\":"<<maximum
                  <<",\"seconds\":"<<seconds<<"}\n";
    }
}
