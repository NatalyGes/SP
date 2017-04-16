import math
C=10**(-6)
L=0.004
U=100
I=U*math.sqrt(C/L)
W=L*I**2/2
print("I=",I,"А")
print("W=",W,"Дж")
