# Creating empty list

l=[]
l1=list()
print(l1)
print(type(l1))
print(l)
print(type(l))

# Add elements to an empty list - Append method is used to add items to a list
l.append(89)
l.append('Hello')
print(l)

# Remove elements from a list

l2=[3,5,6,7,'Hi']
print(l2)
l2.remove(5) #single element remove
print(l2)
l2.clear() # to remove complete list
print(l2)
del l2 # it will remove the entire variable and shows error
print(l2)