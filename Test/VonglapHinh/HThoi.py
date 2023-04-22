h = int(input("Nhập chiều cao: "))

for i in range(1,h-1):
    print(" "*(h - i-1) + "*"*(i*2 - 1))

for j in range(h-1, 0, -1):
    print(" "*(h - j-1) + "*"*(j*2-1))

n = int(input("Nhập độ cao của hình thoi (số lẻ): "))

