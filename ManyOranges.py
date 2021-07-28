import math
A, B, W = map(int, input().split())
W = 1000*W

min_num = math.ceil(W/B)
max_num = math.floor(W/A)

if min_num > max_num:
    print('UNSATISFIABLE')
else:
    print(min_num, max_num)