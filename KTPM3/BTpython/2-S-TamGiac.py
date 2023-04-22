import math
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
if a==b==c:
    p = (a + b + c)/3
    s = ((p**2)*math.sqrt(3))/4
    print("Diện tích tam giác đều là: ",s)
elif a==b!= c:
    eh = c/2
    if a==b < eh:
        h = math.sqrt(eh**2 - b**2 )
        s = (h * c)/2
        print("Diện tích tam giác cân là: ",s)
    elif a==b > eh:
        h = math.sqrt(b ** 2 - eh ** 2)
        s = (h * c) / 2
        print("Diện tích tam giác cân là: ", s)

elif a==c!=b:
    eh = b / 2
    if a==c < eh:
        h = math.sqrt(eh ** 2 - c ** 2)
        s = (h * b) / 2
        print("Diện tích tam giác cân là: ", s)
    elif a==c > eh:
        h = math.sqrt(c ** 2 - eh ** 2)
        s = (h * b) / 2
        print("Diện tích tam giác cân là: ", s)
elif b==c!=a:
    eh = a / 2
    if b==c < eh:
        h = math.sqrt(eh ** 2 - c ** 2)
        s = (h * a) / 2
        print("Diện tích tam giác cân là: ", s)
    elif b==c > eh:
        h = math.sqrt(c ** 2 - eh ** 2)
        s = (h * a) / 2
        print("Diện tích tam giác cân là: ", s)
else:
    p = (a +b +c)/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("Diện tích tam giác thường là: ", s)
