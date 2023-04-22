a = int(input("Nhập vào số nguyên: "))
def snt(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    return False
print('Các số nguyên tố của', a, 'là:')
if a < 2:
    print("Không có số nguyên tố này")
else:
    for i in range(2, a + 1):
        if snt(i):
            print(i, end = " ")
