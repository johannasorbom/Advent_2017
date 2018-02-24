list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
list9 = []
list10 = []
list11 = []
list12 = []
list13 = []
list14 = []
list15 = []
list16 = []
list17 = []

with open('input.txt', 'r') as f:
    content = f.readlines()
    for x in content:
        row = x.split()
        list1.append(int(row[0]))
        list2.append(int(row[1]))
        list3.append(int(row[2]))
        list4.append(int(row[3]))
        list5.append(int(row[4]))
        list6.append(int(row[5]))
        list7.append(int(row[6]))
        list8.append(int(row[7]))
        list9.append(int(row[8]))
        list10.append(int(row[9]))
        list11.append(int(row[10]))
        list12.append(int(row[11]))
        list13.append(int(row[12]))
        list14.append(int(row[13]))
        list15.append(int(row[14]))
        list16.append(int(row[15]))

print(list1)
c = [list1,list2,list3,list4,list5,list6,list7,list8,list9,list10,list11,list12,list13,list14,list15,list16]

for i in range(0,15):
    a = max(c[i])
    b = min(c[i])
    diff = a - b
    list17.append(diff)

summa = sum(list17)
##print(summa)



