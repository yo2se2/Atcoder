N = int(input())
A = set()
B = set()
for _ in range(N):
    s = input()
    if s[0] == '!':
        s.strip()
        B.add(s[1:])
    else:
        A.add(s)
print(A,B)
for i in A:
    if i in B:
        print(i)
        exit()

print('satisfiable')