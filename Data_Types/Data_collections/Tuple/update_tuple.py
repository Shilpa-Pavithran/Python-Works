'''Tuples are unchangeable/immutable, meaning that you cannot change, add, or remove items once the tuple is created.

 but we can add, remove, change it by converting tuple into list and convert back into list to tuple
'''
#Change Tuple Values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#Add Items - method 1 - Convert into a list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

#method 2 - Add tuple to a tuple.
tp = ("apple", "banana")
y = ("pineapple",)
tp = tp+ y
print(tp)

#Remove Items
t1 = ("apple", "banana", "cherry",'orange')
y = list(thistuple)
y.remove("apple")
t1 = tuple(y)
print(t1)


