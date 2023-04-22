#packing và unpacking
lst=['Một hai', 3, 'Bay màu']
def fun1(a, b, c, *,d='die'):
	print(a)
	print(b, c)
	print(d, 'End')

fun1(*lst, d='chết')

def fun2(*arsg, kt):
	print(arsg)
	print(kt)
	print(type(arsg))
fun2(*(x for x in range(5)), kt='sad')

dic={'name':'kt', 	'age':693}
def fun3(a,b):
	print(a)
	print(b)
fun3(*dic)

dic={'name':'kt', 	'age':693}
def fun3(name,age):
	print('tên:', name)
	print('tủi:', age)
fun3(**dic)

def fun4(**sadasd):
	print(sadasd)
	print(type(sadasd))
fun4(name = 'sadas', age= 123)























