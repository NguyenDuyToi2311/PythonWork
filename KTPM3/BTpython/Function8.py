# đệ quy

def fun1(lst):
	if not lst:
		return 0
	else:
		return lst[0] + fun1(lst[1:])

print(fun1([5,8,9,6]))


def fun2(lst):
	return 0 if not lst else lst[0] + fun2(lst[1:])
print(fun2([1,8,6]))
#print(fun2(['8','asd','aaaaa']))


def fun3(lst):
	idx, *r = lst
	return idx if not r else idx + fun3(r)
print(fun3([5,6,8,9])) 
print(fun3(['asdas','asdasd','ccccc']))

def fun4(lst):
	if not lst:
		return 0
	else:
		return fun5(lst)
def fun5(lst):
	return lst[0] + fun4(lst[1:])

print(fun5([4,8,6,4]))






