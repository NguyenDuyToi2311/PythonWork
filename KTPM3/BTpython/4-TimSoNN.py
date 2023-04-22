def fun1(a,b,c,d):
    min = a
    if min > b:
        min = b
    if min > c:
        min = c
    if min > d:
        min = d
    if a==b==c==d:
        print('Các số đều bằng nhau')
    return min
a = int(input("Nhập số: "))
b = int(input("Nhập số: "))
c = int(input("Nhập số: "))
d = int(input("Nhập số: "))
print("Số nhỏ nhất trong 4 số %d, %d, %d, %d là: " % (a,b,c,d), fun1(a,b,c,d))
