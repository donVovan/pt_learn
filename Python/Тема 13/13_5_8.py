# объявление функции
def is_correct_bracket(text):
    ball = 0
    for i in range(len(txt)):
        if ball < 0:
            #print('False')
            break
        if txt[i] == '(':
            ball += 1
        elif txt[i] == ')':
            ball -= 1
    if ball != 0:
        return False
    else:
        return True

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))