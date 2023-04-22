# từ độ F --> độ C (-32 độ + F*(5/9))
# từ độ C --> độ F (32 độ + C*(9/5))

a = float(input("Nhập vào nhiệt bạn muốn đổi: "))
result_CtoF = 9/5 * a + 32
result_FtoC = 5/9 * a - 32

print("Từ {} độ C sang độ F là: {}".format(int(a), result_CtoF))
print("Từ {} độ F sang độ C là: {}".format(int(a), result_FtoC))










