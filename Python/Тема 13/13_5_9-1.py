txt = 'ThisIsCamelCased' #input()
arr = []
for i in txt:
    arr.append(i)
for i in range(len(arr)):
    if arr[i] == arr[i].upper():
        arr[i] = arr[i].lower()
        if i != 0:
            arr.insert(i, '_')
print(''.join(arr))
        
