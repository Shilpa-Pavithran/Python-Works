# program to print list in sort order (ascending and descending)

lst=[5,1,2,7,9,2,7,3]
new=[]
while lst: # when it is empty then only it became false or else it will be true
    min=lst[0]
    for i in lst:
        if i<min:
            min=i
    new.append(min)
    lst.remove(min)
print('ascending order:',new)
print('descending order:',new[::-1])
print(lst)

# using in-built method of sorting in list
l=[15,6,90,3,5]
l.sort()
print('ascending:',l)
l.sort(reverse=True)
print('descending:',l)