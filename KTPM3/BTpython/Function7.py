#Functional tools
from functools import reduce

lst=[-8,-2,0,5,1,-4,2,-5,8,7]

def fun1(x):
	return x+1
print(list(map(fun1, lst)))


lamd = lambda x:x+1
print(list(map(lamd, lst)))


print([lamd(x) for x in lst])


lamd2 = lambda x: x > 0
print(list(filter(lamd2, lst)))
print(list(filter(None, lst)))

print(sorted(lst))

print([x for x in lst if x > 0])

lst2 =[5,3,4,8]
lamd = lambda x,y : x + y
lamd3 = lambda x,y :x * y
print(reduce(lamd, lst2, 23)) #(5+3) + 4 + 8
print(reduce(lamd3, lst2, 20)) # (5 * 3) *4 *8 *20







