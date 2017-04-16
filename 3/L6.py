import math
print("Введите целое число слагаемых")
N=int(input())
print("Введите x")
x=float(input())
S=1
if x==0:
    print("Деление на 0 не предусмотренно в данной системе")
else:
    for i in range(1,N+1):
        S=S+math.cos(i*math.pi/4)*x**i/math.factorial(i)
print("Сумма=",S)
