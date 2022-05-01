from random import randint

print('Добро пожаловать в числовую угадайку')
def is_valid(num):
    num = str(num)
    if num.isdigit():
        num = int(num)
        if num >= 1 and num <= 100:
            return True
        else:
            return False
    else:
        return False
    
def find_number(number, fnd):    
    if number < fnd:
        return 'Ваше число меньше загаданного, попробуйте еще разок'
    elif number > fnd:
        return 'Ваше число больше загаданного, попробуйте еще разок'
    else:
        return 'Вы угадали, поздравляем!'
    
    


q = 'да'
while q == 'да':
    n = randint(1, 100)
    ans = 0
    counter = 0
    while ans != n:
        ans = input('Введите число от 1 до 100: ')
        flag = is_valid(ans)
        if flag:
            ans = int(ans)
            print(find_number(ans, n))
            counter += 1
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
    print(f'Вы угадали с {counter} попытки')
    q = input('Еще партию? Введите "да" для продолжения или любой символ что бы закончить ').lower()
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
