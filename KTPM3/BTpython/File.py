#file_object = open('filetest.txt', mode= 'r', encoding= 'UTF-8')
#data2 = list(file_object)
#file_object.close()
#data3 = file_object.write(' \n ok ổn rồi đó')
#file_object.close()
#data = file_object.read()
#file_object.close()
#print(data3)
#print(data)

with open('filetest2.txt', 'w') as f:
	print('HowKteam', file=f)