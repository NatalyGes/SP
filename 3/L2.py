import math
print("Введите число целое k")
k=int(input("k= "))
W=0
for i in range(-2,k+1):
    if i-4==0:
        W=0
    else:
        W=W+((-1)**i*math.factorial(i+3))/(i-4)
print("Сумма=",W)
    
