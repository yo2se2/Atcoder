N, A, B = map(int, input().split())
S = list(input())
t = A + B

ac = 0
bc = 0

for s in S:
    if (ac + bc) < t:
        if s == 'a':
            print('Yes')
            ac += 1
        elif s == 'b':
            if bc < B:
                print('Yes')
                bc += 1
            else:
                print('No')
        else:
            print('No')
    else:
        print('No')
