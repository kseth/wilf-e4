from math import ceil
from collections import defaultdict

def shape(t,u):
 xs=sorted(set([0.,1.,1+t]+[1+2*t-j for j in range(ceil(1+2*t))]+[t-j for j in range(ceil(t))]))
 ys=sorted(set([0.,1.,1+u]+[u-j for j in range(ceil(u))]+[2*u-j for j in range(ceil(2*u))]))
 xs=[x for x in xs if 0<=x<=1+t];ys=[y for y in ys if 0<=y<=1+u]
 counts=defaultdict(float); mins={}
 for xl,xh in zip(xs,xs[1:]):
  for yl,yh in zip(ys,ys[1:]):
   xm=(xl+xh)/2;ym=(yl+yh)/2
   if not ((xm<1+t and ym<1) or (xm<1 and ym<1+u)):continue
   H=max(0,min(ceil(1+2*t-xm),ceil(u-ym)))
   K=max(0,min(ceil(t-xm),ceil(2*u-ym)))
   I=H,K;count=(xh-xl)*(yh-yl);alpha=xl*(1+3*u)+yl*(2+3*t)
   counts[I]+=count
   mins[I]=min(mins.get(I,float('inf')),alpha)
 return counts,mins

def f(I):h,k=I;return max(3*h-2,3*k-1)
def dual(I):h,k=I;return (h,h-k-1) if h>k else (k-h,k)
def add(I,J):h,k=I;hh,kk=J;return min(h,hh,k+kk+1),min(k,kk,h+hh)
def calc(t,u,T,U):
 ca,ma=shape(t,u);cb,mb=shape(T,U);Q=1+t+u;P=1+T+U
 ga=sum(sum(I)*c for I,c in ca.items());gb=sum(sum(I)*c for I,c in cb.items())
 E=sum(c*d*sum(add(I,J)) for I,c in ca.items() for J,d in cb.items())
 fa=lambda v:min(v%1,1-v%1) if abs(v-round(v))>1e-9 else 1
 # inverse integer bounds on r,s when t=h/r etc: 1/r <= distance(t,Z) unless t integer.
 pen=P*(fa(t)*(1+3*u)+fa(u)*(2+3*t))+Q*(fa(T)*(1+3*U)+fa(U)*(2+3*T))
 base=P*(1+3*u)*(2+3*t)+Q*(1+3*U)*(2+3*T)-2*P*Q+4*P*ga+4*Q*gb-4*E-pen
 cand=[]
 for I,a in ma.items():
  for J,b in mb.items():
   beta=f(I)+f(J)-f(add(dual(I),dual(J)))
   v=base-3*(P*Q*beta+P*a+Q*b)
   cand.append((v,I,J,beta,a,b))
 return max(cand),ca,ma,base

if __name__=='__main__':
 for g in range(1,6):
  for k in range(1,6):
   t=k-.4;u=g-.4
   R=min(ceil(1+2*t),ceil(u)),min(ceil(t),ceil(2*u))
   if R!=(g,k):continue
   best,*_=calc(t,u,t+.1,u-.1)
   print('R',R,'best',best[:4])
