s = input().split()
sum = 0
string = []
for i in s:
    sum += int(i)
for j in range(len(s) - 1):
    string.append(s[j] + '+')
string.append(s[-1] + '=')
string.append(sum)
print(*string, sep='')