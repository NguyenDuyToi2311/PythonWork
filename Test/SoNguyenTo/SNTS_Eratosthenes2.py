# 1 tạo 1 boolean = true để dánh giá các phần tử ban đầu
# 2 cho 0 và 1 false vì kh phải là số nguyên tố
# 3 duyệt qua từng số bằng vòng lặp vs công thức với văng bậc 2 của n
#   1 nếu prime[i] true đánh dấu các bội số i trong khoảng từ i^2 --> n vì các số này kh phải số nguyên tố
# 4 Trả về một list chứa các số nguyên tố từ 2 đến n

def eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [x for x in range(n + 1) if is_prime[x]]


n = int(input("Nhập số n: "))
print(eratosthenes(20))
