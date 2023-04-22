
# Dòng 2: Khởi tạo mảng prime với giá trị True ở tất cả các vị trí từ 0 đến n.
# Ban đầu, tất cả các số đều được giả sử là số nguyên tố.

# Dòng 3: Khởi tạo số nguyên p là 2, đây là số nguyên tố đầu tiên.

# Dòng 4: Bắt đầu vòng lặp while, kiểm tra điều kiện p * p <= n.
# Nếu điều kiện này không được thỏa mãn, tức là p đã vượt quá căn của n,
# và chúng ta không cần xử lý các số nguyên tố lớn hơn nữa.

# Dòng 5: Kiểm tra nếu p là số nguyên tố (tức là prime[p] là True).

# Dòng 6: Với mỗi bội số i của p, đánh dấu prime[i] là False.
# Đây là bước quan trọng nhất của thuật toán Sàng Eratosthenes.
# Chúng ta đánh dấu tất cả các bội số của p là False để loại bỏ các số không phải là số nguyên tố.

# Dòng 7: Tăng giá trị của p lên 1 và tiếp tục vòng lặ

def eratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while p * p <= n:
        if prime[p] == True:
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
    prime = [str(p) for p in range(2, n) if prime[p]]
    prime_str= ", ".join(prime)
    for i in range(0, len(prime_str), 50):
        print(prime_str[i:i + 50])

n = int(input("Nhập n: "))
eratosthenes(n)