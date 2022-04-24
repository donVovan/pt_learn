# объявление функции
def get_factors(num):
    delit = []
    for i in range(1, num + 1):
        if num % i == 0:
            delit.append(i)
    return len(delit)
    

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))