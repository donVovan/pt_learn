n = int(input())
anal = []
for i in range(n):
    anal.append(int(input()))
mn = anal.index(min(anal))
del anal[mn]
mx = anal.index(max(anal))
del anal[mx]
print(*anal, sep='\n')
