a = int(input("Nhập số điểm a: "))
b = int(input("Nhập số điểm b: "))
kq = (a + b)/2
if a and b <0 >10:
    print("Không có điểm này")
if kq < 5:
    print("Học lực Kém điểm: ", kq)
elif 5 >= kq <=7:
    print("Học lực Trung Bình điểm: ", kq)
elif 7 > kq <=8:
    print("Học lực Khá điểm: ", kq)
elif 8> kq <=9.5 :
    print("Học lực Giỏi điểm: ", kq)
else:
    print("Học lực Xuất Sắc điểm: ", kq)
