#!/usr/bin/env node
'use strict';
// Fresh third implementation, 10 September 2026. It was not recovered from
// an earlier message. Computes literal clipped point scores and rectangular
// prefix sums; uses monotone prefix maxima for the horn transition. The
// canonical C++ instead uses closed rectangle/box moment formulas; the
// independent C++ explicitly enumerates every subrectangle transition.
// All arithmetic is exact: inputs and intermediates are integers of absolute
// value below 2^31, hence also below Number.MAX_SAFE_INTEGER.
const fs = require('fs');
const path = require('path');
const assert = require('assert/strict');
const crypto = require('crypto');
const root = path.resolve(__dirname, '..');

function solve(R, p) {
  const n = R + 1, nn = n*n, N = nn*n;
  assert(8 * n*n*n * (9*R+4) < 2**31);
  const idx = (a,b,c) => (a*n+b)*n+c;
  const keep = (a,b,c) => a<p[0] || b<p[1] || c<p[2];
  const horns=[];
  for (let axis=0; axis<3; ++axis) {
    const other=[0,1,2].filter(i=>i!==axis);
    const H=new Int32Array((n+1)*nn);
    const sums=new Int32Array(nn), heights=new Int32Array(nn);
    for (let t=R; t>=0; --t) {
      for (let u=0; u<n; ++u) for (let v=0; v<n; ++v) {
        const x=[0,0,0]; x[axis]=t; x[other[0]]=u; x[other[1]]=v;
        const present=keep(...x), j=u*n+v;
        let sum=present ? 4*(t+u+v)+4-3*R : 0;
        let high=present ? t+u+v : -1;
        if(u) { sum+=sums[j-n]; high=Math.max(high,heights[j-n]); }
        if(v) { sum+=sums[j-1]; high=Math.max(high,heights[j-1]); }
        if(u&&v) sum-=sums[j-n-1];
        sums[j]=sum; heights[j]=high;
        let best=high<=R ? Math.max(0,sum+H[idx(t+1,u,v)]) : 0;
        if(u) best=Math.max(best,H[idx(t,u-1,v)]);
        if(v) best=Math.max(best,H[idx(t,u,v-1)]);
        H[idx(t,u,v)]=best;
      }
    }
    horns.push(H);
  }
  const sums=new Int32Array(N), heights=new Int32Array(N);
  let best=-(2**30);
  for(let a=0;a<n;++a) for(let b=0;b<n;++b) for(let c=0;c<n;++c) {
    const present=keep(a,b,c);
    let sum=present ? 4*(a+b+c)+4-3*R : 0;
    let high=present ? a+b+c : -1;
    for(let mask=1;mask<8;++mask) {
      const aa=a-((mask&1)?1:0),bb=b-((mask&2)?1:0),cc=c-((mask&4)?1:0);
      if(aa<0||bb<0||cc<0) continue;
      const bits=((mask&1)?1:0)+((mask&2)?1:0)+((mask&4)?1:0);
      sum+=(bits%2?1:-1)*sums[idx(aa,bb,cc)];
      high=Math.max(high,heights[idx(aa,bb,cc)]);
    }
    sums[idx(a,b,c)]=sum; heights[idx(a,b,c)]=high;
    if(high<=R) best=Math.max(best,sum+horns[0][idx(a+1,b,c)]
      +horns[1][idx(b+1,a,c)]+horns[2][idx(c+1,a,b)]);
  }
  assert(Number.isSafeInteger(best));
  return best;
}

const names=['canonical_strip.txt','independent_strip.txt'];
const paths=names.map(name=>path.join(root,'round6','uniform_gap',name));
const texts=paths.map(p=>fs.readFileSync(p,'utf8'));
assert.equal(texts[0],texts[1],'Prior implementations disagree');
const records=texts[0].trim().split('\n').map(l=>l.trim().split(/\s+/).map(Number));
const expected=[];
for(let R=18;R<=21;++R) for(let a=1;a<=R+1;++a)
  for(let b=a;b<=R+1;++b) for(let c=b;c<=R+1;++c)
    if(a+b+c<=R+1) expected.push([R,a,b,c]);
assert.deepEqual(records.map(r=>r.slice(0,4)),expected);
assert.equal(expected.length,1029);
const compute=!process.argv.includes('--records-only');
const rows=[], summary=[];
for(let R=18;R<=21;++R) {
  const selected=records.filter(row=>row[0]===R);
  for(const row of selected) {
    const [r,a,b,c,score]=row;
    const actual=compute ? solve(r,[a,b,c]) : score;
    assert.equal(actual,score,`Mismatch at ${[r,a,b,c]}`);
    assert(actual<=0);
    rows.push([r,a,b,c,actual]);
  }
  const maximum=Math.max(...selected.map(row=>row[4]));
  assert.equal(maximum,4-3*R);
  const result={R,corner_configurations:selected.length,maximum};
  summary.push(result);
  process.stderr.write(JSON.stringify(result)+'\n');
}

// Exact rational identities in the analytic bridge, using BigInt only.
// 4/21 - 3/(2*21) = 5/42.
assert.equal(4n*2n-3n,5n);
// 42*2*v*(5-v) - 5*(1+6*v+v^2) = -5+390*v-89*v^2.
assert.deepEqual([-5n,42n*10n-30n,-84n-5n],[-5n,390n,-89n]);
assert.equal(80n*79n*78n/6n,82160n);
// q(H)=5H^2-390H+89 is increasing for H>=78 and q(78)=89>0.
assert.equal(5n*78n*78n-390n*78n+89n,89n);
const report={status:'passed',fresh_javascript_full_recomputation:compute,
  rows:rows.length,per_R:summary,arithmetic:'exact bounded integers; analytic identities use BigInt',
  source_sha256:crypto.createHash('sha256').update(fs.readFileSync(__filename)).digest('hex'),
  compared_files:paths.map((p,i)=>({path:path.relative(root,p),sha256:crypto.createHash('sha256').update(texts[i]).digest('hex')})),
  continuous_gap:'5/42',strict_multiplicity_cutoff:82161};
if(compute) fs.writeFileSync(path.join(__dirname,'uniform_gap_js_strip.txt'),rows.map(r=>r.join(' ')).join('\n')+'\n');
fs.writeFileSync(path.join(__dirname,'uniform_gap_verification.json'),JSON.stringify(report,null,2)+'\n');
process.stdout.write(JSON.stringify(report,null,2)+'\n');
