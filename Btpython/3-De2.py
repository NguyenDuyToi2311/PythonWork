# nhập vào một số và tính giai thừa từ 1 đến N giai thừa
n = int(input("sdaasd: "))
def giaithua(n):
    if n == 0:
        return 1
    return n * giaithua(n-1)

print(giaithua(n))
