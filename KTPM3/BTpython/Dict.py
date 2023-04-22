dic1 = dict(name='duy', member= 69, slow= 'hahha')
dic2 = {'name':'hola', 'member': 12, 'slow': 'haaaaahha'}
print(dic1)
print(dic2)

inter = ('name', 'haha')
dic = dict.fromkeys(inter, 'okbaby')
dic['name'] = 'hohoho'
print(dic)


dic = dict(d = 'duy', n = 'non', num = 2000)
dic['num'] += 1
dic['d'] = dic['d'] + ' slow'

print(dic)