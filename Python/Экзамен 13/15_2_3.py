from random import randint
n = randint(1, 100)
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

number = input('Введите число от 1 до 100: ')
if is_valid(number):
    while number != n:
        if is_valid(number) > n:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Ваше число меньше загаданного, попробуйте еще разок:')
        number = input('Введите число от 1 до 100: ')
    print('Вы угадали, поздравляем!')
    
else:
    print('А может быть все-таки введем целое число от 1 до 100?')
    number = input('Введите число от 1 до 100: ')




# 'Ваше число меньше загаданного, попробуйте еще разок: '
# 'Ваше число больше загаданного, попробуйте еще разок '
# print('Вы угадали, поздравляем!')        
#number = input('Введите число от 1 до 100: ')
#if is_valid(number):
#    pass        
#else:
#        print('А может быть все-таки введем целое число от 1 до 100?')
        