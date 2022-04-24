txt = '())(()'
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
    print('False')
else:
    print('True')