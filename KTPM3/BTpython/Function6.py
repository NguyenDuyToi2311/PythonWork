#LamBda



def fun1():
	kq = lambda x: x + ' is protected'
	return kq
b = fun1()	
print(b('haha'))

lamda = [lambda x: x**2, lambda x: x**4, lambda x: x**6]

for n in lamda:
	print(n(3))










