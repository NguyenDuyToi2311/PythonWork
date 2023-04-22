#lenght = 3
#inter = (x for x in range(3))
#c = 0
#while c < lenght:
	#c += 1
#	try:
#		print(next(inter))
#	except StopIteration:
#		break


	
#for n in range(2):
#	print(type(n))
#for k in range(5):
#	if k % 2 == 0 :
		#break 
#		continue
#	print(k)
#else:
#	print('End')

#range[start, end, step]
#print(list(range(10, -21, -2)))

lst=[1,2,3]
for value in lst:
	value+= 1
print(lst)

lst2= [1,2,3]
for value in range(len(lst2)):
	lst2[value] +=1
print(lst2)

#[ output-expression for-statement optional-predicate ]
lst3= ['--'.join((a.capitalize(), b.upper() + c.lower())) for a, b, c in [('how', 'kteam', 'EDUCATION'), ('chia', 'sẻ', 'FREE')]]
print(lst3)

lst4 =[]
for a,b,c in [('how', 'kteam', 'EDUCATION'), ('chia', 'sẻ', 'FREE')]:
	a = a.capitalize()
	b = b.upper()
	c = c.lower()
	lst4.append('--'.join((a,b+c)))
print(lst4)

lst5 = {key:value + 1 for key, value in (('Kteam', 69), ('Tèo', 50), ('Tũn', 14), ('Free Education', 93)) if value % 2 != 0}
print(lst5)

lst6 = {}
for key, value in (('Kteam', 69), ('Tèo', 50), ('Tũn', 14), ('Free Education', 93)):
	if value % 9 != 0:
		lst6[key] = value + 1
	print(lst6)

studen = ['Long', 'Trung', 'Giàu', 'Thành']
for stu in studen:
	print(stu, end= " ")
#enumerate(iterable[, start])
for idx, stu2 in enumerate(studen,0):
	print(idx,'=>', stu2)






























