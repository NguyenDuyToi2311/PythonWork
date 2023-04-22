n = int(input("Nhập dãy số: "))
ma = 0

for i in range(n):

    khoangtrang = " "*((n - i) * 4 - 1)
    print(khoangtrang, end = "")
    #print(i)
    for j in range(i*2+1):
        print(str(ma).rjust(3), end = " ")
        ma += 1
    print()