#Yield
def fun1(lst):
	#sq_lst = []
	for num in lst:
		#sq_lst.append(num**2)
	#return sq_lst
		yield num**2
for n in fun1([3,5,9]):
	print(n)


def fun2():
	for n in range(5):
		print('cộng', n + 1, "trừ")
		yield n
for n in fun2():
	print(n)		



def fun3():
    yield 'Kteam'
    print('this is the second yield')
    yield 'Free education'
    print('this is the last yield')
    yield 'Long đẹp trai'
    print('Will not return anything')
for value in fun3():
    print(value)

def fun4():
	while True:
		x = yield
		yield x ** 2
g = fun4()
print(next(g))
print(g.send(2))
print(next(g))
print(g.send(10))








