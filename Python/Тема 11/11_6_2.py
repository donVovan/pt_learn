str = input()
str = str.split()
numb = []
for i in str:
    i = int(i)
    numb.append(i)
str_min = min(numb)
min_pos = numb.index(str_min)
str_max = max(numb)
max_pos = numb.index(str_max)
numb[min_pos] = str_max
numb[max_pos] = str_min
print(*numb)
