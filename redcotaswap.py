#転倒数を求める問題

S = input()

d = {'a':0,'t':1,'c':2,'o':3,'d':4,'e':5,'r':6}
L = []

#文字列を数字にしてリスト化
for s in S:
    L.append(d[s])

def bubble_sort(l):
    cnt = 0
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j] <= l[j+1]:
                continue
            else:
                l[j], l[j+1] = l[j+1], l[j]
                cnt += 1
    return cnt

ans = bubble_sort(L)
print(ans)