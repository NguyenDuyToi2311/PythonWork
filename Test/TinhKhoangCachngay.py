#Ngày vào ngày, tháng. Hãy tính và in ra xem ngày nhập vào cách ngày đầu năm bao nhiêu ngày
# (giả sư năm đó không phải là năm nhuận)
# Tạo dictionary số ngày của các tháng trong năm không nhuận

days_in_month_1 = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
days_in_month_2 = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
# Nhập vào ngày và tháng
a = int(input("Năm: "))
b = int(input("Tháng: "))
c = int(input("Ngày: "))

# Tính số ngày từ đầu năm đến tháng trước tháng nhập vào
total_days = 0
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    for i in range(1, b):
        total_days += days_in_month_1[i]
        # total_day = 0 + range(days_in_month)
else:
    for i in range(1, b):
        total_days += days_in_month_2[i]
        # total_day = 0 + range(days_in_month)
total_days += c - 1

end_days = 0
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    for i in range(b, 13):
        end_days += days_in_month_1[i]
else:
    for i in range(b, 13):
        end_days += days_in_month_2[i]

# Cộng thêm số ngày của tháng nhập vào và trừ đi 1
end_days -= c
# In ra kết quả
print("Ngày hiện tại cách ngày đầu của năm là {} và còn {} ngày là hết năm".format(total_days, end_days))


