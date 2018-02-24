f = open ( 'input.txt' , 'r')
l = []
d = []
l = [line.split() for line in f]
c = [list(map(int, x)) for x in l]

for i in range (0,15):
    for x in range (0,15):
        for a in range (0,15):
            if (c[i][x] % c[i][a]) == 0:
                b = (c[i][x]/c[i][a])
                d.append(b)
     
summa = sum(d)        
print(summa)

