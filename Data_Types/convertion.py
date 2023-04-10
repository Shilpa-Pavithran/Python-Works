# converting set to list and tuple
s={1,2,3}
print(list(s))
print(tuple(s))

# Adding element to an tuple -method1
t=(1,2,3)
t1=4,
print(t+t1)

# method2
y=list(t)
y.append(4)
print(tuple(y))

# how to print the last element form a set
s={23,5,6,8,9,1,0,87}
y=list(s)
print(y[-1])

# how will you remove duplicate elements from a list
#  using set()
l=[1,3,4,5,2,3,3,1,2,6,5,7,4]
s=list(set(l))
print(s)