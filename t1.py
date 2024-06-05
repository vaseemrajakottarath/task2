l1 =[{'a':10,'a2':10},{'b':2},{'c':3}]
sum_of = 0

for i in range(len(l1)):
    for key,value in l1[i].items():
        sum_of += value
print(sum_of)