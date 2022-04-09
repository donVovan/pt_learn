s = input()
s = s.split()
counter = 0
for i in s:
    for j in s:
        if i == j:
            counter += 1
counter = (counter - len(s)) // 2
print(counter)
