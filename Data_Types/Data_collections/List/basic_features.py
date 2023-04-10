'''''
Lists are created using square brackets:

* List items are ordered, (changeable - mutable),
* allow duplicate values.
* List items are indexed, the first item has index [0], the second item has index [1] etc.
* heterogeneous - can be of different datas (integer, float, tuple, string , dict, set etc..)
* nesting possible
* Using the list() constructor to make a List:

'''

l=[2,4,'hi',9.8,(1,2,3),False,{2,4,5},2,4,'hi',5,{1:2,2:3}] # Heterogeneous elements ,ordered, and allows duplicate
print(l)
print(type(l))
print(len(l)) # len() used to check the length of list
print(l[4]) # support indexing
print(l[3:10]) # support slicing
for i in l:
    print(i)

l1=[25,89,30.8,[1,3,5]] #nesting possible
print(l1)