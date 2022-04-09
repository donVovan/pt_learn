s = '3 2 1 2 2 4 3 2 5 3 2' #input()
s = s.split()
counter = 0
for i in s:
    for j in s:
        if i == j:
            counter += 1
counter = (counter - len(s)) // 2

