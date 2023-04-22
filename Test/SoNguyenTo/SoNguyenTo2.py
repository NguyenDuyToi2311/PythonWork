def is_prime(n):
    if n < 2:
        return False
    # int để ép giá trị số
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input("Nhập số n: "))
s = [str(i) for i in range(2, n) if is_prime(i)]
print(", ".join(s))