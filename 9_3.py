s = input()
count = 0
numb = '0123456789'
for i in range(len(s)):
    if s[i] not in numb  and s[i] == s[i].lower():
        count += 1
print(count)
