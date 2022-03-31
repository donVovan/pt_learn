s = input()
find_f = s.count('f')
if find_f == 0:
    print('NO')
elif find_f == 1:
    print(s.find('f'))
else:
    print(s.find('f'), s.rfind('f'))
