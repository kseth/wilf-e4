import json,itertools,array,collections,pathlib,sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
PERMS=list(itertools.permutations(range(3)))
def trans(k,p):
 if k<343:
  v=(k//49,k//7%7,k%7);return 49*v[p[0]]+7*v[p[1]]+v[p[2]]
 if k<346:return 343+p.index(k-343)
 return k
def canon(ids):return min(tuple(sorted(trans(k,p) for k in ids)) for p in PERMS)
def summarize(c):
 total=sum(c.values());vals=sorted(c.values(),reverse=True);cumul=0;qs={}
 for k,v in enumerate(vals,1):
  cumul+=v
  for target in (50,75,90,95,99,100):
   if target not in qs and cumul*100>=target*total:qs[target]=k
 return {'distinct':len(c),'assigned_shapes':total,'families_needed_by_recorded_assignment_percent':qs,'top_10_coverage':sum(vals[:10]),'top_100_coverage':sum(vals[:100]),'top_20':[{'columns':list(x),'assigned_shapes':v} for x,v in c.most_common(20)]}
joined=collections.Counter();out={};categories=collections.Counter();all_ids=set()
for name,folder in [('original','round7/low_degree6'),('supplementary','round8/simplification')]:
 rows=[json.loads(s) for s in (ROOT/folder/'dual_bases.jsonl').read_text().splitlines()];bases={r['id']:tuple(r['columns']) for r in rows};data=array.array('I');data.frombytes((ROOT/folder/'dual_assignments.bin').read_bytes())
 if sys.byteorder!='little':data.byteswap()
 counts=collections.Counter(data);raw=collections.Counter();sym=collections.Counter()
 for k,n in counts.items():
  b=bases[k];raw[b]+=n;sym[canon(b)]+=n;joined[b]+=n;all_ids.update(b);categories[(sum(x<343 for x in b),sum(343<=x<346 for x in b),346 in b,347 in b)]+=n
 out[name]={'registry_bases':len(rows),'used_registry_bases':len(counts),'raw':summarize(raw),'coordinate_symmetry':summarize(sym)}
canonjoined=collections.Counter()
for b,n in joined.items():canonjoined[canon(b)]+=n
out['combined']={'raw':summarize(joined),'coordinate_symmetry':summarize(canonjoined),'column_categories':[{'point_columns':k[0],'weight_bound_columns':k[1],'H_lower':k[2],'H_upper':k[3],'assigned_shapes':v} for k,v in categories.most_common()],'unique_point_columns':len([x for x in all_ids if x<343])}
(ROOT/'round9/dual_compression_statistics.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({name:{k:v for k,v in obj.items() if k not in ('raw','coordinate_symmetry')}|{kind:{k:v for k,v in obj[kind].items() if k!='top_20'} for kind in ('raw','coordinate_symmetry')}for name,obj in out.items()},indent=2))
