height = 4
width = 6

for i in range(height):
    for j in range(height-i-1):
        print(" ", end="")
    for j in range(width):
        print("*", end="")
    print()