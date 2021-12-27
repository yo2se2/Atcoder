S = input()
f = True
l = []
uc = 0
dc = 0
for s in S:
    if f:
        if s == '<':
            uc += 1
        elif s == '>':
            l.append(uc)
            uc = 0
            dc = 1
            f = False
    else:
        if s == '>':
            dc += 1
        elif s == '<':
            l.append(dc)
            dc = 0
            uc = 1
            f = True
l.append(max(uc,dc))


def sum_arith(x):
    return int(x*(1+x)/2)

if len(l) % 2 != 0:
    l.append(1)
ans = 0

for i in range(0,len(l),2):
    # print(l[i],l[i+1])
    ans += sum_arith(max(l[i],l[i+1]))
    ans += sum_arith(min(l[i],l[i+1])-1)

print(ans)