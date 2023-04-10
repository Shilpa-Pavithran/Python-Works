#program to print minimum and maximum element from a list

l=[8,4,2,9,1,6]
min=l[0]  # min=8, min=4, min=2, min=1
for i in l:
    if i<min: # 8<8, 4<8, 4<2,2<9, 2<1, 1<6 iteration stops and exit from loop
        min=i # min=4, min=2, min=1 - last min value is 1
print('minimum',min)

max=l[0]
for i in l:
    if i>max:
        max=i
print('maximum',max)