s = input()
s = s.split()
fio = []
for i in s:
    fio.append(i[0])
fio = '.'.join(fio)
print(fio, end='.')
