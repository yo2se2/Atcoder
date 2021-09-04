N = int(input())
ans = 'DRAW'
dic = []
for i in range(N):
    w = input()
    if i > 0:
        lw = dic[i-1][-1]
        print("最初の文字は　{}　でなければならない。".format(lw))
        if w[0] != lw:
            if i % 2 == 0:
                ans = 'LOSE'
                break
            else:
                ans = 'WIN'
                break

        elif w in dic:
            if i % 2 == 0:
                ans = 'LOSE'
                break
            else:
                ans = 'WIN'
                break

    dic.append(w)

print(ans)
