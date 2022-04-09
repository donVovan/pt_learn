strings = []
keys = []
n = int(input())
for i in range(n):
    strings.append(input())
k = int(input())
for i in range(k):
    keys.append(input().upper())
for string in strings:
    for key in keys:
        if key not in string.upper():
            break
    else:
        print(string)
