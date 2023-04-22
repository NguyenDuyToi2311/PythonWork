soA = input('Nhập vào một dãy số dùng dấu cách: ')

space = soA.split()

dsso = map(int, space)
tongds = sum(dsso)
print(tongds)
