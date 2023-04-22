from time import sleep 
print('Cái gì đó', 'nó lạ lắm', 'đấy nhé', sep=' - ')
print('chuẩn bị dùng end')

print('star...', end='', flush=True)
sleep(5)
print('end...')

your_name = "Henry"
your_great = "Hello! My name is "

for c in your_great + your_name:
    print(c, end='', flush=True)
    sleep(0.1)
print()	