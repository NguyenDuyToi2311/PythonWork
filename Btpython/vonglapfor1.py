n = int(input("Nhập dãy số: "))
ma = 0
ks = 0
kt = 2

for i in range(n):
    while kt <= len(str(n)) + 2:
        kt += 1
    #khoangtrang = " "*(((n - i) * kt - 1 )-len(str(n)) - 2)
    #khoangtrang = " " * (n - i - 1) * 2
    #print(khoangtrang, end = "")
    for j in range(i*2+1):
        while kt > ks + 1:
            ks += 1
        khoangso = str(ma).rjust(ks)
        print(khoangso, end = " ")
        ma += 1
    print()

