a = input("Nhập vào Tuple (dùng cách để tách phần tử): ")
tpl = tuple(a.split())

print("Tuple là: ", tpl, "\nType: ", type(tpl))
# thêm phần tử vào tuple ===================
b = input("Mời bạn thêm phần tử cho Tuple: ")
tpl2 = tuple(b.split())
# thêm trong tuple dùng += thay vì dùng exptend, append===================
tpl += (tpl2)
print(tpl)

# xóa phần tử trong tuple =================================================
lst = list(tpl)
lst2 = len(lst)
c = input("Nhập vị trí phẩn tử cần xóa thứ: ")
if c.isdigit():
    if  0 <= int(c) <= lst2:
        lst.pop(int(c))
        print("Bạn vừa xóa phần tử thứ: ", c)
        print("Tuple hiện tại: ", tuple(lst))
    else:
        print("Vị trí phần tử nằm ngoài Tuple")
else:
    print("Tuple hiện không có vị trí phần tử là chữ")
#==========================================================================
tpl3 = tuple(lst)
d = input("Nhập vào ký tự cần đếm: ")
rs = tpl.count(d)
print("Ký tự", d ,"có %d phần tử trong tuple"% (rs))
print("Số phần tử trong tuple là: ",len(tpl3))

