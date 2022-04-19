L = input().split()
M = input().split()
sum = []
for i, j in zip(L, M):
    sum.append(int(i) + int(j))
print(*sum)