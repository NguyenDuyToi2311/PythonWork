#five_even_numbers = []
#k_number = 1
#while len(five_even_numbers) < 5:
#    if k_number % 2 == 0:
#        five_even_numbers.append(k_number)
#    k_number += 1
#print(five_even_numbers)
#print(k_number)



a = [56, 14, 11, 756, 34, 90, 11, 11, 65, 0, 11, 35]

#vị trí bắt đầu để xử lý chuỗi
idx = 0
#lấy độ dài chuỗi làm mốc kết thúc từ phải qua trái
maidx = len(a) - 1
#lấy độ dài từ trái qua phải
majdx = len(a)

while idx < majdx:
    if a[idx] == 11:
        idx += 1
        continue
    jdx = idx + 1

    while jdx < majdx:
        if a[jdx] == 11:
            jdx += 1
            continue
        #phần tử idx > hơn jdx thì gán cả 2 bằng nhau
        if a[idx] > a[jdx]:
            a[idx], a[jdx] = a[jdx], a[idx]
        jdx += 1
    idx += 1
print(a)