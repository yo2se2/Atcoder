W = list(input())

'abcde'
ans = []

for w in W:
    if w in 'aiueo':
        continue
    else:
        ans.append(w)
print(''.join(ans))


