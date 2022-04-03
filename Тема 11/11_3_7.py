n = int(input())
full = [1]
for i in range(n):
    full.append(int(input()))

del full[::2]
print(full)
