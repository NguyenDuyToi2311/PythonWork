from time import sleep
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
kq = -b/a

str = "Phương trình %dx + %d= 0 " % (a,b)
str2 = "\nKết quả x = ", kq
for x in str:
    print(x, end="")
    sleep(0.2)
for x in str2:
    print(x, end="")
    sleep(0.2)
