a, b = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

pin = ['x' for _ in range(10)]

for i in p:
    pin[i] = '.'
for j in q:
    pin[j] = 'o'

print('{} {} {} {}'.format(pin[7],pin[8],pin[9],pin[0]))
print(' {} {} {}'.format(pin[4],pin[5],pin[6]))
print('  {} {}  '.format(pin[2],pin[3]))
print('   {} '.format(pin[1]))