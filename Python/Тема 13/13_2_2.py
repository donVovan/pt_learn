# объявление функции
def print_fio(name, surname, patronymic):
    n = name[0].upper()
    s = surname[0].upper()
    p = patronymic[0].upper()
    print(s,n,p, sep='')

# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name, surname, patronymic)