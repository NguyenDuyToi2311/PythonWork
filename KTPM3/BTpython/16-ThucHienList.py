from time import sleep
a = input("Nhập vào List (dùng cách để tách phần tử): ")
lst = list(a.split())

print("List là: ", lst, "\nType: ", type(lst))

b = input("Mời bạn thêm phần tử cho list: ")
lst.extend(list(b.split()))
print("List hiện tại: ", lst)

# xóa phần tử list theo số phần tữ nhập vào ========================================
lst2 = len(lst)
c = input("Nhập vị trí phẩn tử cần xóa thứ: ")
if c.isdigit():
    if  0 <= int(c) <= lst2:
        lst.pop(int(c))
        print("Bạn vừa xóa phần tử thứ: ", c)
        print("List hiện tại: ", lst)
    else:
        print("Vị trí phần tử nằm ngoài List")
else:
    print("List hiện không có vị trí phần tử là chữ")
# xóa phần tử list theo số phần tữ nhập vào ========================================
sleep(3)
print("\n",lst)
d = input("Nhập vào ký tự cần đếm: ")
rs = lst.count(d)
print("Ký tự", d ,"có %d phần tử trong list"% (rs))

lst.reverse()
print("Đảo ngược list:\n",lst)

lst.sort(reverse=True)
print("List tăng dần:\n",sorted(lst))

print("List giảm dần:\n",lst)



