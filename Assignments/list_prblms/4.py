# 4.write a python program to find the common numbers from two lists
l1=[1,2,5,4,8,3]
l2=[5,9,4,7,6,8]
l=[]
for i in l1:
    for j in l2:
        if i==j:
            l.append(j)
print('common numbers from the lists:',l)


