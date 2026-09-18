import numpy as np, json

def P(x,y):
    return x**3/6-x**4/4+x*y*y/2-3*x*x*y*y/4-x*y**3/2

def Q(u,v):
    x,y=min(u,v),max(u,v)
    k=min(x,(1-y)/2)
    def F(z):
        return y*(-z**3/2+(1+1.5*y)*z*z/2-y*z)
    return P(k,y)+F(x+y)-F(k+y)

def run(N):
    s=np.arange(N+1)/N
    xx,yy=np.meshgrid(s,s,indexing='ij')
    rr=xx+yy; aa=xx*yy
    q=np.zeros((N+1,N+1)); v=q.copy(); one=q.copy(); path={}
    largest=0; bad=None
    for n in range(N+1):
        for i in range(n+1):
            j=n-i
            q[i,j]=Q(i/N,j/N)
            vv=v[:i+1,:j+1]+(1-1.5*n/N)*(n/N-rr[:i+1,:j+1])*aa[:i+1,:j+1]
            oq=q[:i+1,:j+1]+(1-1.5*n/N)*(n/N-rr[:i+1,:j+1])*aa[:i+1,:j+1]
            one[i,j]=max(q[i,j],float(np.max(oq)))
            ix=np.unravel_index(np.argmax(vv),vv.shape)
            v[i,j]=max(q[i,j],float(vv[ix]))
            if v[i,j]>q[i,j]+1e-12:path[(i,j)]=ix
            gap=v[i,j]-one[i,j]
            if gap>largest+1e-12:
                largest=gap; bad=(i,j)
    chain=[]
    if bad:
        cur=bad
        while cur in path:
            chain.append(cur);cur=path[cur]
        chain.append(cur)
    return {'N':N,'max_gap':largest,'bad':bad,'chain':chain,'V':float(v[bad]) if bad else None,'one_jump':float(one[bad]) if bad else None}

if __name__=='__main__':
    out=[run(n) for n in [40,80,160]]
    print(json.dumps(out,indent=2))
    open('round3/no_interior/slack_bridge_probe.json','w').write(json.dumps(out,indent=2))
