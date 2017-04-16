print("Введите натуральное число N")
N=int(input("N="))
print("Делители числа ",N,":")
a=[ i for i in range(1,N+1) if (N % i == 0)]
a.reverse()
print(a)
