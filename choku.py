X = input()
lx = list(X)
lang = ('',  'o', 'k', 'u')

def is_choku(x: list):
    L = len(x)
    i = 0
    while L > i:
        a = x[i]
        if a == 'c':
            b = x[i]+x[i+1]
            if b == 'ch':
                i += 2
                continue
            else:
                return 'NO'
        elif a in lang:
            i += 1
        else:
            return 'NO'
    return 'YES'

print(is_choku(lx))