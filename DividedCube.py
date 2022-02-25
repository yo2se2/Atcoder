A, B, C =map(int, input().split())

ans1 = abs(A*B*(C//2) - A*B*(C-C//2))
ans2 = abs(B*C*(A//2) - B*C*(A-A//2))
ans3 = abs(C*A*(B//2) - C*A*(B-B//2))

print(min(ans1,ans2,ans3))