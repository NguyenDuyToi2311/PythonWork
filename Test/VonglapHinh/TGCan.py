h = int(input("Nhập chiều cao: "))

for i in range(1,h):
    print(" "*(h - i-1) + "*"*(i*2-1))
