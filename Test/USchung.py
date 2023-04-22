

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

def uc(a, b):
    if b == 0:
        return a
    return uc(b, a%b)

g = uc(a, b)
#for i in range(1, g + 1):
#    if g%i == 0:
#        print(i)

rs = [str(i) for i in range(1, g + 1) if g%i ==0]
num = ", ".join(filter(lambda x:x != '',rs))
print("Ước Chung của 2 số {}, {} là: {}".format(a,b,num))
