def plus(a):
    lst = list(a)
    lst.reverse()
    b = "".join(lst)
    return b
a = input("Nhập chuỗi: ")
print("Chuỗi đão ngược là: ", plus(a))
