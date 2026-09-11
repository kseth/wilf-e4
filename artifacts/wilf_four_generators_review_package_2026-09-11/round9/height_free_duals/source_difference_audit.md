# Exact source changes for the height-free certificate

Both changes preserve the previous finite coverage and exact arithmetic implementation. The new independent verifier is still implemented separately from the producer.

```diff
--- round7/low_degree6/certify_all.cpp
+++ round9/height_free_duals/certify_height_free.cpp
@@ -41,7 +41,7 @@
  return out;
 }
 int main(int argc,char**argv){
- string dir=argc>1?argv[1]:"round7/low_degree6";
+ string dir=argc>1?argv[1]:"round9/height_free_duals";
  ofstream out(dir+"/unused.tsv"),fails(dir+"/certification_failure.tsv"),stats(dir+"/certification.jsonl");
  basis_output.open(dir+"/dual_bases.jsonl");assignment_output.open(dir+"/dual_assignments.bin",ios::binary);
  out<<"pid\txy\txz\tyz\tm\tdegree\tunit_D\terosion\n";fails<<"pid\txy\txz\tyz\tm\tdegree\tunit_D\terosion\n";
@@ -71,7 +71,7 @@
     int e=A.count()+(A&fx).count()+(A&fy).count()+(A&fz).count();if(e>m)continue;erosionok++;
     auto F0=T&(~(T>>49)|bx),F1=T&(~(T>>7)|by),F2=T&(~(T>>1)|bz);
     if((F1&F2).count()>2*a->hx || (F0&F2).count()>2*a->hy || (F0&F1).count()>2*b->hy)continue;qok++;
-    int maxima=(F0&F1&F2).count();if(maxima<=6){sixmax++;continue;}remaining++;hist[m]++;
+    int maxima=(F0&F1&F2).count();if(maxima<=6){sixmax++;}remaining++;hist[m]++;
     int R=0,sum=0;for(int d=1;d<=6;d++){int cnt=(T&layers[d]).count();if(cnt)R=d;sum+=d*cnt;}
     int D=3*m*R-4*sum;smallestMargin=min(smallestMargin,10*D-10*m+29);
     
@@ -86,12 +86,12 @@
      for(size_t index=K._Find_first();index<K.size();index=K._Find_next(index))Z.push_back(index);
      vector<vector<double>>mat;vector<double>rhs;
      for(int id:Z){int x=id/49,y=(id/7)%7,z=id%7;mat.push_back({double(x),double(y),double(z),-1});rhs.push_back(-x-y-z);}
-     mat.push_back({0,0,0,1});rhs.push_back(7);
+     // No upper bound on H: height-free centroid certificate.
      vector<double>obj={4.0*S[0],4.0*S[1],4.0*S[2],-3.0*m},solution;
      ProposingLP lp(mat,rhs,obj);if(!lp.solve(solution)){cerr<<"LP failure\n";return 2;}
      int at=0;for(int var:lp.N)if(var!=-1){
       if(var<4)chosen[at++]=343+var;
-      else {int i=var-4;chosen[at++]=(i<(int)Z.size()?Z[i]:347);}
+      else {int i=var-4;if(i>=(int)Z.size()){cerr<<"Unexpected height-upper column";return 4;}chosen[at++]=Z[i];}
      }
      if(at!=4){cerr<<"basis size failure\n";return 3;}
      ok=exact_dual(chosen,m,S,margin_num,denom);
```

```diff
--- round7/low_degree6/independent_verify.cpp
+++ round9/height_free_duals/independent_verify_height_free.cpp
@@ -59,7 +59,7 @@
     require(z[0]==(I)bs.size(),"basis ids not consecutive");
     Basis b;M a{};
     for(int j=0;j<4;++j){
-      b.ids[j]=z[j+1];if(j)require(b.ids[j-1]<b.ids[j],"basis columns not strictly increasing");
+      b.ids[j]=z[j+1];require(b.ids[j]!=347,"height upper bound forbidden");if(j)require(b.ids[j-1]<b.ids[j],"basis columns not strictly increasing");
       auto c=column(b.ids[j]);for(int i=0;i<4;++i)a[i][j]=c[i];
     }
     I d=determinant(a);require(d!=0,"singular basis");
@@ -115,7 +115,7 @@
 };
 int main(int argc,char**argv){
  try{
-  const std::string dir=argc>1?argv[1]:"round7/low_degree6";
+  const std::string dir=argc>1?argv[1]:"round9/height_free_duals";
   const auto bs=read_bases(dir);const auto planes=make_planes();
   std::ifstream assignments(dir+"/dual_assignments.bin",std::ios::binary);
   require(bool(assignments),"missing assignments");
@@ -170,7 +170,7 @@
         for(int i=0;i<7;++i){nx+=H[i][0]>0;ny+=H[0][i]>0;}
         require(nx==a->nx&&ny==a->ny&&nz==b->ny,"axis agreement");
         if(Qxy>2*nz||Qxz>2*ny||Qyz>2*nx)continue;++count.q_ok;
-        if(K<=6){++count.six_maxima;continue;}
+        if(K<=6){++count.six_maxima;}
         ++count.remaining;++total;++count.hist[m];
         int D=3*m*R-4*(Sx+Sy+Sz);
         count.min_unit=std::min(count.min_unit,10*D-10*m+29);
@@ -212,7 +212,7 @@
     std::cerr<<"pid "<<pid<<" verified "<<count.remaining<<" exact weighted duals; compatible "<<count.compatible<<"\n";
   }
   require(assignments.peek()==std::char_traits<char>::eof(),"extra assignment bytes remain");
-  require(total==3361434,"unexpected total remaining shapes");
+  require(total==3742041,"unexpected total remaining shapes");
   std::cout<<"{\"status\":\"passed\",\"profiles\":"<<planes.size()<<",\"bases\":"<<bs.size()
     <<",\"exact_weighted_duals\":"<<total<<",\"floating_point_used\":false}\n";
  }catch(const std::exception&e){std::cerr<<"FAIL: "<<e.what()<<"\n";return 1;}
```
