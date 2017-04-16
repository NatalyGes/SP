import math
y=0
for x in (1,3,0.2):
    y=y+(x**3+4*x**2+2)
print("Сумма всех y на промежутке от 1 до 3 с шагом 0.2 =",y)
def p1(): 
    x = 1
    while x <= 3:
        print (round(x,2), "\t", x**3+4*x**2+2)
        x += 0.2
print("  X       Y    ")
p1() 
