n = int(input("Nhập số giai thừa: "))
def giaiThua(n):
    if n == 0:
        return 1
    return n * giaiThua(n - 1)
print(giaiThua(n))