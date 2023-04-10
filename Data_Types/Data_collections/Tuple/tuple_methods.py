''' Only 2 methods used in tuple'''
# count() - Returns the number of times a specified value occurs in a tuple
# index()	- Searches the tuple for a specified value and returns the position of where it was found

t=['a','p','p','l','e']
print(t.count('p'))
print(t.index("l"))

# Built-in functions using tuple
print(max(t))
print(min(t))
print(len(t))

''' To join two or more tuples you can use the + operator'''

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply Tuples

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)


