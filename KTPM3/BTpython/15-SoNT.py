
import math
def Num(a):
    tg = int(math.sqrt(a))
    for i in range(2, tg + 1):
        if (a % i) == 0:
            return False
    return True

n = int(input('Nhập số: '))
print('Các số nguyên tố của', n, 'là:')
if n < 2:
    print("Không có số nguyên tố này")
else:
    for i in range(2, n + 1):
        if Num(i):
            print(i, end=" ")














# kiểm tra xem có phải số nguyên tố không
#def is_prime(n):
#    count = 0
#    for i in range(1, n + 1):
#        if n % i == 0:
#            count += 1
#    if count == 2:
#        return True
#    return False
#n = int(input())
#print(is_prime(n))