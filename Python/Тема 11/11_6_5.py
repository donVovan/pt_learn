s = input()
arr = []
s = s.split()
for i in s:
    i = int(i)
    arr.append(i)
arr.sort()
print(*arr)
arr.sort(reverse = True)
print(*arr)
