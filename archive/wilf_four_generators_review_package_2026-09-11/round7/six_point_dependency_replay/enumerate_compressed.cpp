#include <algorithm>
#include <array>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;
using Point=array<int,3>;
using Shape=vector<Point>;

int score(const Shape& z) {
    int k=z.size(), e=0, projections=0;
    for(int j=0;j<3;j++) {
        int mx=0;
        for(auto p:z){e+=p[j];mx=max(mx,p[j]);}
        e-=mx;
        set<pair<int,int>> pr;
        for(auto p:z)
            for(int u=0;u<=p[(j+1)%3];u++)
                for(int v=0;v<=p[(j+2)%3];v++) pr.insert({u,v});
        projections+=pr.size();
    }
    return projections-3*k-e;
}

Shape canonical(const Shape& z) {
    array<int,3> perm={0,1,2};Shape best;
    do {
        Shape c;
        for(auto p:z)c.push_back({p[perm[0]],p[perm[1]],p[perm[2]]});
        sort(c.begin(),c.end());
        if(best.empty() || c<best)best=c;
    }while(next_permutation(perm.begin(),perm.end()));
    return best;
}

int main(int argc,char** argv) {
    int k=argc>1?stoi(argv[1]):5;
    vector<vector<int>> seq,ordered;
    long long lim=1;for(int i=0;i<k;i++)lim*=k;
    for(long long code=0;code<lim;code++) {
        auto n=code;vector<int> a(k);int mask=0,mx=0;
        for(int j=0;j<k;j++){a[j]=n%k;n/=k;mask|=1<<a[j];mx=max(mx,a[j]);}
        if(mask!=((1<<(mx+1))-1))continue;
        seq.push_back(a);
        if(is_sorted(a.begin(),a.end()))ordered.push_back(a);
    }
    set<Shape> all,negative;
    for(auto x:ordered)for(auto y:seq)for(auto zc:seq) {
        Shape z(k);bool ok=true;
        for(int i=0;i<k;i++)z[i]={x[i],y[i],zc[i]};
        for(int i=0;i<k && ok;i++)for(int j=0;j<i;j++) {
            if(!(z[j]<z[i])) {ok=false;break;}
            bool lt=false,gt=false;
            for(int c=0;c<3;c++){lt|=z[j][c]<z[i][c];gt|=z[j][c]>z[i][c];}
            if(!(lt && gt)){ok=false;break;}
        }
        if(!ok)continue;
        auto c=canonical(z);
        if(all.insert(c).second && score(c)<0)negative.insert(c);
    }
    map<int,int> hist;
    for(auto z:all)hist[score(z)]++;
    cerr<<"k="<<k<<" sequences="<<seq.size()<<" canonical="<<all.size()<<" negative="<<negative.size()<<" histogram=";
    for(auto [s,n]:hist)cerr<<s<<":"<<n<<",";
    cerr<<"\n";
    cout<<"[";bool first=true;
    for(auto z:negative) {
        if(!first)cout<<",";first=false;
        cout<<"[";
        for(int i=0;i<k;i++){if(i)cout<<",";cout<<"["<<z[i][0]<<","<<z[i][1]<<","<<z[i][2]<<"]";}
        cout<<"]";
    }
    cout<<"]\n";
}
