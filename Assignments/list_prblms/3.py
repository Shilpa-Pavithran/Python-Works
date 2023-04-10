# 3.write a python program to find largest number in a given list with out using max()

l1=[45,18,95,71,481,68,124,231]
largest=l1[0]
for i in l1:
    if i>largest:
        largest=i
print('largest number: ',largest)