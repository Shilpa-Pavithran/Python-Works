# Program to print common elements from the given set

s1={1,2,3,4,5}
s2={3,4,5,6,7}
for i in s1:
    if i in s2:
        print(i)

s1={1,2,3,4,5}
s2={3,4,5,6,7}
common=set()
for i in s1:
    if i in s2:
        common.add(i)
print(common)


