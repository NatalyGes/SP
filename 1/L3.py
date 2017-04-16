import math
x=int(input("введите число x= "))
b=int(input("введите число b= "))
a=int(input("введите число a= "))
y=int(input("введите число y= "))
K=(math.sqrt(x+b-a)+math.log10(y))/(math.atan(b+a))
print(K)
