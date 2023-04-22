n = int(input("Nhập nhập: "))
s = 0
for i in range(1, n):
    s += i
print(f"S = {' + '.join(map(str, range(1, n + 1))) } \n <=> {s}")







