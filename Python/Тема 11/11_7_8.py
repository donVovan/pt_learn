#s = 'Число Pi примерно равно 3.1415' #input()
#for i in s:
#    if i.isdigit():
#        print(i, end='')

#numb = [i for i in s if i.isdigit()]
print(*[i for i in input() if i.isdigit()], sep='')
    