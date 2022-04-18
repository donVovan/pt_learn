#s = '1 2 3 4 5 6 7 8 9'#input()
#s = s.split()
#for i in s:
#    i = int(i)
#    if i % 2 == 0:
#        i = i ** 2        
#        if i % 10 != 4:
#            print(i)
#sqv = [int(i) ** 2 for i in input().split() if int(i) % 2 == 0 and int(i) ** 2 % 10 != 4]
print(*[int(i) ** 2 for i in input().split() if int(i) % 2 == 0 and int(i) ** 2 % 10 != 4])
        