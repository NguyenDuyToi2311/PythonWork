#s = 'How Kteam'
## vị trí bắt đầu bạn muốn xử lí của chuỗi
#idx = 0 
## lấy độ dài chuỗi làm mốc kết thúc
#length = len(s)

#while idx < length:
#    print(idx, 'stands for', s[idx])
#    idx += 1




five_even_numbers = []
k_number = 1
while True:     
	# nếu k_number là một số chẵn
    if k_number % 2 == 0: 
		# thêm giá trị của k_number vào list
        five_even_numbers.append(k_number)
    	# nếu list này đủ 5 phần tử
        if len(five_even_numbers) == 5: 
    	# thì kết thúc vòng lặp
        	break
    k_number += 1
print(five_even_numbers)
print(k_number) 



#k_number = 0
#while k_number < 10:
#	k_number += 1
#	if k_number % 2 ==0:
#		continue
#	print(k_number, ' số' )
#print(k_number)	


	

