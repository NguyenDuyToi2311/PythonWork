num1 = int(input("Nhập số a: "))
num2 = int(input("Nhập số b: "))
# tìm các ước chung của 1 số ============================================
print("Các số ước chung của %d là: "%(num1))
for i1 in range(1,num1+1):
    if num1 % i1 ==0:
        print(i1, end=" ")
print("\nCác số ước chung của %d là: "%(num2))
for i2 in range(1,num2+1):
    if num2 % i2 ==0:
        print(i2, end=" ")
# tìm ước chung lớn nhất của 2 số nhập vào
def UCLN(soA, soB):
    while soA != soB:
        if soA > soB:
            soA = soA - soB
        else:
            soB = soB - soA
    return soB
print("\nƯớc số chung lớn nhất của %d và %d là: %d"%(num1,num2,UCLN(num1,num2)))

