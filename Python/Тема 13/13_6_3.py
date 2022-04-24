# объявление функции
def solve(a, b, c):
    D = b ** 2 - 4 * a * c
    if D < 0:
        return 'Нет корней'
    elif D == 0:
        return (-b - D ** 0.5) / (2 * a)
    else:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        return min(x1, x2), max(x1, x2)

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)