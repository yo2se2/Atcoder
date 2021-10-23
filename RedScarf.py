N = int(input())
A = list(map(int,input().split()))
"""
x1 ^ x2 ^ x3 ^ x4 = B
     x2 ^ x3 ^ x4 = A1
 
"""
B = 0
for a in A:
    B ^= a
x = []
for a in A:
    x.append(str(B^a))

print(' '.join(x))