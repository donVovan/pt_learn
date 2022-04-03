n = int(input())
counter = 0
for i in range(n):
    i = input()
    if i.count('11') >= 3:
        counter += 1
print(counter)
