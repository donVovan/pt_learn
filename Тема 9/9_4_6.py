s = input()
counter = 0
more_letter = s[0]
for i in range(len(s)):
    chair = s.count(s[i])
    if chair >= counter:
        counter = chair
        more_letter = s[i]
print(more_letter)        
