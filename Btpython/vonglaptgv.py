n = int(input("Nhập số cần lặp: "))

for row in range(n):
	for col in range(n - row, 0, -1 ):
		print(col, end = " ")
	print("")