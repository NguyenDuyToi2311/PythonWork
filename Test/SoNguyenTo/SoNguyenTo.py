# dùng function để sử lý
# điểm yếu là chạy code tính được số nguyên tố trong các số int(bit)

# tức là số càng cao càng khó tính ra kết quả
# ngắn gọn dễ hiểu
# công thức số nguyên tố là chỉ chia hết cho 1, chia hết cho chính nó, không được chia hết cho các số nhỏ hơn
def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return "Đây là số nguyên tố"
    return "Đây không phải là số nguyên tố"
n = int(input("Nhập số nguyên tố cần kiểm tra: "))
print(is_prime(n))