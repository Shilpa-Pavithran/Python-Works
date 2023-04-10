# odd or even using list comprehension

l=[1,2,3,4,5,6,7,8,9,10]
even=[i for i in l if i%2==0]
odd=[i for i in l if i%2!=0]
print(even)
print(odd)

# Changing elements using list comprehension
lst=[100,200,250,300,500]
newlst=[i if i!=250 else 150 for i in lst]
print(newlst)