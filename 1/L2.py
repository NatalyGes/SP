import math
y=int(input("введите число y= "))
i=int(input("введите число i= "))
L=(0.81*math.cos(i))/(math.log10(y)+2*i**3)
print(L)
