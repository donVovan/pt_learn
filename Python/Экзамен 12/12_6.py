#s = 'проспал почти всю ночь'.split()
#for i in s:
#    new = i[1:] + i[0] + 'ки'
    
print(*[i[1:] + i[0] + 'ки' for i in input().split()])
    