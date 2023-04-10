# How to create empty set
s=set()
print(s)
print(type(s))

# To add an elements to an empty set
s.add(5)
s.add('Hi') # (. dot) vechu call cheyunathu methods anu, dot illathe call cheyunathu functions
s.add(89.58)
s.add(True)
print(s)

# To remove single elements from a set
s1={1,0.5,5,89,75,48}
print(s1)
s1.remove(89) # remove() is used to remove single element in a set
print(s1)
s1.clear() #  clear() to remove all elements from a set
print(s1)
del s1 # it will delete the entire variable. it will display error message
print(s1)
