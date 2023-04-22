# cách 2

a = int(input("Nhập năm: "))
b = int(input("Nhập tháng: "))

if b == 2:
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        day = 28
    else:
        day = 29
elif b in [4, 6, 9, 11]:
    day = 30
else:
    day = 31
print("Năm {} có tháng {} là {} ngày".format(a, b, day))