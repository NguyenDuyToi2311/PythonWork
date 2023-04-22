a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

def uscln(a,b):
    if b == 0:
        return a
    return uscln(b, a % b)
def bscnn(a,b):
    return int((a * b) / uscln(a, b))

print("Các ước số của {} là: {}" )
for i in range(1, a):
    if a % i == 0:
        print(i, end=" ")
print("\nCác ước số của {} là: {}" )
for i in range(1,b):
    if b % i == 0:
        print(i, end=" ")

print("\nƯớc số chung của 2 số {}, {} là: ")
g = uscln(a, b)
for i in range(1, g+1):
    if g%i == 0:
        print(i, end= " ")

print("\nBội số chung nhỏ nhất của 2 số {}, {} là: " )
print(bscnn(a,b))

print("\nƯớc số chung lớn nhất của 2 số {}, {} là: " )
print(uscln(a,b))




