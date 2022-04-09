n = int(input())
negative = []
nulls = []
positive = []
for i in range(n):
    i = int(input())
    if i < 0:
        negative.append(i)
    elif i > 0:
        positive.append(i)
    else:
        nulls.append(i)
print(*negative, sep='\n')
print(*nulls, sep='\n')
print(*positive, sep='\n')