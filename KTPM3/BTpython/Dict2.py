d = {'key': 'Value', (1,2):69}
print(d)

d2 = d.clear()
print(d2)
value = d.get('key')
print(value)

value2 = d.values()
print(value2)

value3= d.setdefault('hola', 'hello')
value4 = d.update(key='NewValue', newkey='newtext')

print(value4)
print(d)



