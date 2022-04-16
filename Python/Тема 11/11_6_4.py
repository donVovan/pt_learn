n = input()
n = int(n[1:])
for i in range(n):
    s = input()
    if '#' in s:
        ind = s.find('#')
        s = s[:ind]
        s = s.rstrip()
        print(s)
    else:
        s = s.rstrip()
        print(s)
        
    
