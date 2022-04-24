# объявление функции
def convert_to_python_case(text):
    arr = []
    for i in txt:
        arr.append(i)
    for i in range(len(arr)):
        if arr[i] == arr[i].upper():
            arr[i] = arr[i].lower()
            if i != 0:
                arr.insert(i, '_')
    return ''.join(arr)

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))