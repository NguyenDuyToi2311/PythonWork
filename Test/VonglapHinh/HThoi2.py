n = 10
# Vẽ phần trên của hình thoi
for i in range(n//2+1):
    print(" "*(n//2-i) + "*"*(2*i+1))
print()
# Vẽ phần dưới của hình thoi
for i in range(n//2, 0, -1):
    print(" "*(n//2-i+1) + "*"*(2*i-1))