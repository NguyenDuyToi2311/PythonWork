
n = int(input("n = "))
char = 65
x = n- 1
line = 0
for i in range(1, n*n - x*x + 1,2):
    print("  "*x, end = "")
    for j in range(1, i + 1):
        print(chr(char), end = " ")
        char += 1
        if char > 90:
            char = 65
    x -= 1
    print()


