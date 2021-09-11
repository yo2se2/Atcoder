s = list(input())
k = int(input())
L = len(s)

A = set()
for i in range(L-k+1):
    A.add(''.join(s[i:i+k]))
print(len(A))