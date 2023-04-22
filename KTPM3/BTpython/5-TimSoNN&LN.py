def fun1(a,b,c,d):
    max = a
    min = c
    if max < b: max = b
    if max < c: max = c
    if max < d: max = d
    if min > b: min = b
    if min > a: min = a
    if min > d: min = d
    if a == b == c == d:
        print('Các số đều bằng nhau')
    return max, min
a = int(input("Nhập số: "))
b = int(input("Nhập số: "))
c = int(input("Nhập số: "))
d = int(input("Nhập số: "))
print("Số lớn nhất và nhỏ nhất trong 4 số %d, %d, %d, %d là: " % (a,b,c,d), fun1(a,b,c,d))