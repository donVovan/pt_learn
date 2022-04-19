tel = input()
tel_new = tel.replace('-', '')
flag = False
if tel_new.isdigit() == False:
    flag = False
else:
    tel = tel.split('-')
    et = []
    for i in tel:
        et.append(len(i))
    if et == [1, 3, 3, 4] and tel[0] == '7':
        flag = True
    elif et == [3, 3, 4]:
        flag = True

if flag == False:
    print('NO')
else:
    print('YES')