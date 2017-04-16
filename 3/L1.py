print("Введите натуральное число N")
N=int(input("N="))
b=0
a=[i for i in range(1,N+1) if 3*i>N]
S=len(a)
if S==0:
    print("Таких чисел нет")
else:
    print("Min=",min(a))
    K=3*min(a)
    print("3*min=",K)    
