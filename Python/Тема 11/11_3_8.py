n = int(input())
s = []
for i in range(n):
    s.append(input())
k = int(input()) - 1
new = []
for j in range(len(s)):
    if len(s[j]) > k:
        print(s[j][k], end='')
