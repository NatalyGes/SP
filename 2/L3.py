import math
print("Введите координату x: ")
x=float(input("x= "))
print("Введите координату y: ")
y=float(input("y= "))
r_xy=math.sqrt(x**2+y**2)
r_xy1=math.sqrt((x+1)**2+y**2)
if r_xy<=2 and r_xy1>=1:
    print("Точка принадлежит графику")
else:
     print("Точка не принадлежит графику")
