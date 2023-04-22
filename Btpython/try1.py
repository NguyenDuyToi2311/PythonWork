def kiemtraHoanHao(n):
    tong = 0
    for i in range(1,n):
        for j in range(1, i):
            if (i % j) == 0:
                tong += j
		if tong == n:
			return True
		else:
			return False


n = int(input('Nhap vao so nguyen n lon hon 0: '))
if kiemtraHoanHao(n):
    print(n, ' la so hoan hao')
else:
    print(n, ' khong la so hoan hao')