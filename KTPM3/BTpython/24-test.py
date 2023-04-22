arrA = []
arrB = []
def ucln(a,b):
    if(b == 0):
        print("Ước chung lớn nhất: ",a)
    elif(a == 0):
        print("Ước chung lớn nhất: ", b)
    else:
        for i in range(0,a):
            if(a % (i + 1)== 0 ):
                arrA.append(i + 1)
        print("a: ",arrA)
        for j in range(0,b):
            if(b % (j + 1)== 0 ):
                arrB.append(j + 1)
        print("b: ", arrB)
        print("Ước chung lớn nhất: ",max(set(arrA) & set(arrB)))
A = int(input("Nhập số a: "))
B = int(input("Nhập số b: "))
ucln(A,B)
