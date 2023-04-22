a = int(input())
b = int(input())

dem = 0
for i in range(a, b + 1):
    if i % 5 == 0:
        dem += 1
        if dem > 10:
            print("\nIn qua 10 so roi!")
            break
        print(i, end=" ")
else:
    if dem == 0:
        print("Khong co so nao chia het cho 5")
    else:
        print("\nDa in het cac so chia het cho 5")