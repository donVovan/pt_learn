n = int(input())
d = []
s = []
for i in range(1, n + 1):
    d.append(int(input()))
for j in range(1, len(d)):
    s.append(d[j - 1] + d[j])    
print(s)
