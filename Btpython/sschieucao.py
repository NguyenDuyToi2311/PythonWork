ten1, chieucao1 = input('Nhập tên và chiều cao: ').split()

ten2, chieucao2 = input('Nhập tên và chiều cao: ').split()


try:
    chieucao1 = int(chieucao1)
    chieucao2 = int(chieucao2)
    if chieucao1 <= 0 or chieucao2 <= 0:
        print("Chiều hơn phải lớn hơn 0")
    elif chieucao1 == chieucao2:
        print("Cả %s và %s đều bằng nhau".format(ten1, ten2))
    elif chieucao1 > chieucao2:
        print(ten1 + ' cao hơn ' + ten2)
    else:
        print(ten2, ' cao hơn ', ten1)
except:
    print("Đầu vào kh hợp lệ !!!")