# объявление функции
def is_magic(date):
    arr = date.split('.')
    year = int(arr[2]) % 100
        
    
    if int(arr[0]) * int(arr[1]) == year:
        return True
    else:
        return False

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))