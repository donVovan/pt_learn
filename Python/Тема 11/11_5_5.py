s = input()
s = s.split('.')
flag = True
for i in s:
    i = int(i)
    if i < 0 or i > 255:
        flag = False
        break
if flag:
    print('ДА')
else:
    print('НЕТ')
