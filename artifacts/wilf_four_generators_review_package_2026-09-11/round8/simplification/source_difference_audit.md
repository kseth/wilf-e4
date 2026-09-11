# Source difference audit

11 September 2026.

The supplementary producer and separately implemented verifier have exactly the following changes from their previous sources. Header copies are byte-identical. The maxima predicates partition all surviving shapes into disjoint exhaustive classes: the original certificate accepts `K>6`, while this supplement accepts `K<=6`. No shape-selection condition before this partition and no exact certificate arithmetic changes.

## Producer

```diff
--- original
+++ supplement
@@ -71,7 +71,7 @@
     int e=A.count()+(A&fx).count()+(A&fy).count()+(A&fz).count();if(e>m)continue;erosionok++;
     auto F0=T&(~(T>>49)|bx),F1=T&(~(T>>7)|by),F2=T&(~(T>>1)|bz);
     if((F1&F2).count()>2*a->hx || (F0&F2).count()>2*a->hy || (F0&F1).count()>2*b->hy)continue;qok++;
-    int maxima=(F0&F1&F2).count();if(maxima<=6){sixmax++;continue;}remaining++;hist[m]++;
+    int maxima=(F0&F1&F2).count();if(maxima>6){continue;}sixmax++;remaining++;hist[m]++;
     int R=0,sum=0;for(int d=1;d<=6;d++){int cnt=(T&layers[d]).count();if(cnt)R=d;sum+=d*cnt;}
     int D=3*m*R-4*sum;smallestMargin=min(smallestMargin,10*D-10*m+29);
     
```

## Independent verifier

```diff
--- original
+++ supplement
@@ -170,7 +170,8 @@
         for(int i=0;i<7;++i){nx+=H[i][0]>0;ny+=H[0][i]>0;}
         require(nx==a->nx&&ny==a->ny&&nz==b->ny,"axis agreement");
         if(Qxy>2*nz||Qxz>2*ny||Qyz>2*nx)continue;++count.q_ok;
-        if(K<=6){++count.six_maxima;continue;}
+        if(K>6)continue;
+        ++count.six_maxima;
         ++count.remaining;++total;++count.hist[m];
         int D=3*m*R-4*(Sx+Sy+Sz);
         count.min_unit=std::min(count.min_unit,10*D-10*m+29);
@@ -212,7 +213,7 @@
     std::cerr<<"pid "<<pid<<" verified "<<count.remaining<<" exact weighted duals; compatible "<<count.compatible<<"\n";
   }
   require(assignments.peek()==std::char_traits<char>::eof(),"extra assignment bytes remain");
-  require(total==3361434,"unexpected total remaining shapes");
+  require(total==380607,"unexpected total previously skipped shapes");
   std::cout<<"{\"status\":\"passed\",\"profiles\":"<<planes.size()<<",\"bases\":"<<bs.size()
     <<",\"exact_weighted_duals\":"<<total<<",\"floating_point_used\":false}\n";
  }catch(const std::exception&e){std::cerr<<"FAIL: "<<e.what()<<"\n";return 1;}
```

Both original source files remain unchanged. The assignment count changes because the selected class is complementary. The original default output directory string remains unchanged in the copied sources; every documented invocation and the Python entry point supplies the supplementary directory explicitly.
