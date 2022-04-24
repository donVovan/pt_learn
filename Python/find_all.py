# объявление функции
def find_all(target, symbol):
    place = []
    for i in range(len(target)):
        if target[i] == symbol:
            place.append(i)
    return place
            

# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))