tup = (1,8,6, ' hahaha', 8)
tup2 = ( i for i in range(10) if i%2 ==0)
kq = tuple(tup2)
print(kq)

tup3 = (5,8,9,4)
tup3 += (4,88,5)
kq2 = 4 in tup3
# lấy kết quả index
kq3 = tup3[5]
# thêm phần tử vào tuple
kq4 = tup3.index(5)
print(kq4)
