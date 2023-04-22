h = int(input("Nhập chiều cao: "))

for i in range(1,h):
    print(" "*(2*h - 2*i - 2) + "*"*(2*i-1))
