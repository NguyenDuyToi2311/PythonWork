import math
from fractions import Fraction
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
def fun1(a,b,c):
    delta = b**2 - 4 * a * c
    if a==0:
        kq = -c / b
        print("Do a = 0 phương trình có dạng bậc 1, x = ", kq)
    elif delta > 0:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print("Có 2 nghiệm phân biệt: \n x1 = %f \n x2 = %f" % (x1,x2))
    if delta == 0:
        x3 = -b /(2*a)
        print("Có nghiệm kép: x1 = x2 = ",x3)
    if delta < 0:
        str = "Phương trình vô nghiệm"
        print(str)
print("Phương trình bậc 2 có dạng %dX^2 + %dX +%d = 0"% (a,b,c))
fun1(a,b,c)
