print("Введите целое число N")
N=int(input("N="))
print("Числа кратные 5 из промежутка от 1 до",N,":")
a=[i for i in range(1,N+1) if i%5==0]
if len(a)==0:
    print("Таких чисел нет")
else:
    print(a)
    
      
