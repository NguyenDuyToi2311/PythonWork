def fibonacci(n):
    if n < 1:
        return 0
    elif n == 0 or n ==1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

a = int(input("Nhập vào dãy fibonacci: "))
fbc = ""
for i in range(0, a):
    fbc = fbc + str(fibonacci(i))+", "

print("Dãy fibonacci là: ", fbc)