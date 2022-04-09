s = input()
counter = 0
for i in range(len(s)):
    if s[i].isdigit() == True:
        counter += 1
print(counter)
    