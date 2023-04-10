# Data Collection - are used to store multiple items in a single variable. Types Set, dict, list, tuple

''''A set is a collection of items which is unordered,unchangeable*, and unindexed.
* Do not support duplicate values.
* The elements (are heterogeneous) can be of different types (integer, float, tuple, string )
* set is mutable. We can add or remove  items from it.
* A set is created by placing all the elements inside curly braces {},
separated by comma or by using the built-in function set().
* nesting not possible
* cannot use {} empty curly braces because it calls as dict. instead we can use set()
* set cannot have element like - list, set or dictionary, as its element. it will occur error

set operations like union, intersection, symmetric difference etc. - is used to perform the mathematical set operation
'''

s1={9,'New',5,10,0.25,'Hi',28,5,10, False,True,9,(1,2,3)}
print(s1)
print(type(s1))
for i in s1:
    print(i)
# len() fucntion used to check the length of set
print(len(s1))

# s2={25,35,20,{1,34,5}}  #nesting not possible in sets. Type error shows
# print(s2)
#
# s3={[1,2,3]} #A set cannot contain lists. Type error shows
# print(s3)

# We can convert a list to set  using set function
s4=set([12,3,95])
print(s4)
print(type(s4))

