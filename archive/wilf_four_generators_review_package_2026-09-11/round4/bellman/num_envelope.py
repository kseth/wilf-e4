import sys
sys.path.insert(0,'round3/no_interior')
from probe_slack_bridge import Q
import numpy as np
from scipy.optimize import differential_evolution
for B,C in [(.15,.8),(.4,.4),(.3,.6),(.45,.5),(.1,.6),(.15,.7),(.24,.7),(.05,.9),(.48,.48)]:
 r=B+C
 def f(z):
  x,y=z;return Q(x,y)+(1-1.5*r)*(r-x-y)*x*y
 out=differential_evolution(lambda z:-f(z),[(0,B),(0,C)],tol=1e-11,seed=1)
 print(B,C,'value',-out.fun,'caps',out.x,'Q',Q(B,C))
