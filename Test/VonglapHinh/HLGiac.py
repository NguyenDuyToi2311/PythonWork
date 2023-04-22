n = int(input("Nhập N: "))


# cho vòng lặp đầu chạy từ i - n
# trong đó vòng lặp i sẽ chạy theo (i + j)%10
# (2 + 5) % 10 = 7, vậy ta có vòng lặp lớn thứ 2 tại vị trí vòng lặp nhỏ thứ 5 là 7
# i[2] j[5] = 7
for i in range(n):
    for j in range(10):
        num = (i+j) % 10
        print(num, end="")
    print()





