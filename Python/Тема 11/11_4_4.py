n = int(input())
s = []
for i in range(n):
    i = input()
    if i not in s:
        s.append(i)
print(*s, sep='\n')
