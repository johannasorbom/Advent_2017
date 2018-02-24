f = open ( 'input.txt' , 'r')
l = []
d = []
l = [line.split() for line in f]
c = [list(map(int, x)) for x in l]

for i in range(0,16):
    a = max(c[i])
    b = min(c[i])
    diff = a - b
    d.append(diff)

summa = sum(d)
print(summa)
