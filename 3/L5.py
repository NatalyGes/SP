print("Введите последовательность чисел через "," ")
a=[float(i) for i in input().split(',')]
s=0
i=0
while i <=len(a):
    if a[i]!=0:
        if a[i]>0:
            s=s+a[i]
            i=i+1
    else:
        i=len(a)+1
print("Сумма положительных элементов ряда, до первого вхождения 0 =",s)
        
