nam = int(input("Nhập vào năm: "))
thang = int(input("Nhập vào tháng: "))
th ={1:31, 3:31, 5:31, 7:31, 9:31, 10:31, 12:31, 2:29, 4:30, 6:30, 8:30, 11:30}
th2 ={1:31, 3:31, 5:31, 7:31, 9:31, 10:31, 12:31, 2:28, 4:30, 6:30, 8:30, 11:30}
namn = th[thang]
namkn = th2[thang]
if nam % 4 == 0:
    if nam % 100 ==0:
        if nam % 400 ==0:
            tnam = True
        else:
            tnam = False
    else:
        tnam = True
else:
    tnam = False

if tnam == True:
    print("Năm %d là năm nhuần có 366 ngày và có tháng %d là %d ngày " % (nam, thang, namn))
else:
    print("Năm %d là năm không nhuần có 365 ngày, có tháng %d là %d ngày " % (nam, thang, namkn))
