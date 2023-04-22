# năm nhuận chia hết cho 4 hoặc 400 và kh chia hết cho 100

# cách 1 đơn giản và dùng dict để làm ngày tháng
a = int(input("Nhập năm: "))
b = int(input("Nhập tháng: "))
dic_month_1 = {1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 10: 31, 12: 31, 2: 28, 4: 30, 6: 30, 9: 30, 11: 30}
dic_month_2 = {1: 31, 3: 31, 5: 31, 7: 31, 8: 31, 10: 31, 12: 31, 2: 29, 4: 30, 6: 30, 9: 30, 11: 30}
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print("Năm {} nhuận, tháng {} có {} ngày".format(a, b, dic_month_2[b]))
else:
    print("Năm {} không nhuận, tháng {} có {} ngày".format(a, b, dic_month_1[b]))

