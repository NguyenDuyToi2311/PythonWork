n = int(input("Nhập n: "))
rs = [str(i) for i in range(1,n+1) if n%i == 0 ]
num = ', '.join(filter(lambda x: x != '',rs))
print("Toàn bộ ước số của {} là: {}".format(n, num))