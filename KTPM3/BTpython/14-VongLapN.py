n = int(input("Nhập số n: "))
for row in reversed(range(1, n + 1)):
    for col in reversed(range(1, row + 1)):
        print(col, end=' ')
    print("")
print("End, Bye.")
