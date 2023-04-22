#positional
def function(text, age):
	print(text)
	print(age)

function('mày nói gì cơ', 69)

def f(kteam=[]):
	kteam.append('F')
	print(kteam)
f()

def function2(a, b):
	pass
function2(5, 'sda')

def function3(a, b, c, d):
	f= a +b +c +d
	print(f)
function3(5,6,8,3)

def function4(pos_key, *, key_arg, key_arg2):
	print(pos_key)
	print(key_arg)
	print(key_arg2)
function4(1, key_arg='h', key_arg2= 23)


