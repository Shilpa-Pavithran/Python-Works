# To print odd or even using set
s={1,2,4,5,6,7,8,87,54,23,12}
even=set()
odd=set()
for i in s:
    if i%2==0:
        even.add(i)
    else:
        odd.add(i)
print('Even set:',even)
print('Odd set:',odd)