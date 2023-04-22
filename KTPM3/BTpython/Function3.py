#local và globals

#def fun():
#	k = 'haha'
#	print('kết quả,',k)
#fun()
lst = ['How Kteam', 4, 8]

def change(parameter):
    parameter[0] = 'New value'
    print('Changed successfully!')

print(lst)
change(lst)
print(lst)

def fun2_global():
	global x
	x = 1
def fun3_local():
	x = 5 
	print('đây là x: ', x)

fun2_global()
print(x)
fun3_local()
print()

print(locals())
print(globals())










