H, W = map(int,input().split())

for _ in range(H):
    s = list(input())
    for i in range(len(s)-1):
        if s[i] == 'T' and s[i+1]== 'T':
            s[i],s[i+1] = 'P','C'
    print(''.join(s))


