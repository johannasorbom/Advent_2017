##f = open ( 'input.txt' , 'r')
##l = []
##d = []
##l = [line.split() for line in f]
##c = [list(map(int, x)) for x in l]
##for i in range (16):
##    for x in range (16):
##        for a in range (16):
##            if (c[i][x] % c[i][a]) == 0:
##                b = (c[i][x]/c[i][a])
##                d.append(b)
##
##summa = sum(d)        
##print(summa)

#Test
l = [[444],[444],[422]]
for i in range (3):
    for x in range (3):
        for a in range (3):
            if (c[i][x] % c[i][a]) == 0:
                b = (c[i][x]/c[i][a])
                d.append(b)

summa = sum(d)        
print(summa)
