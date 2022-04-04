#n = int(input())
#text = []
#for i in range(n):
#    text.append(input())
text = ['Язык Python прекрасен', 'C# - отличный язык программирования', 'Stepik - отличная платформа', 'BEEGEEK FOREVER!', 'язык Python появился 20 февраля 1991']

k = 2 #int(input())
z_search = ['ЯЗЫК', 'PYTHON'] #[]
#for z in range(k):
#    z_search.append(input().upper())
#flag = 0
z_search = (" ".join(z_search))
for j in range(len(text)):
    #for s in range(len(z_search)):
        
    if z_search in text[j].upper():
            #flag += 1
        #if flag % 2 == 0:
            print(text[j])
#for q in range(k):
#    q = input().upper()
#for j in range(len(text)):
#    if y in text[j].upper():
#        print(text[j])
#print(z_search)
