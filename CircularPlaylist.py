N, T = map(int, input().split())
A = list(map(int, input().split()))

#累積和
cs = [0]
t = 0
for a in A:
    t += a
    cs.append(t)

dt = T % cs[-1]

for i in range(1,N+1):
    if dt > cs[i]:
        continue
    else:
        play_list = i
        Time = dt - cs[i-1]
        break
print(play_list,Time)