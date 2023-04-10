# 7. write a python program to remove repeated elements from a given list without using built-in methods
l1=[2,5,5,6,7,8,2,6,8,9,1,2]
print(l1)
new=[]
for i in l1:
    if i not in new:
        new.append(i)
print(new)


# # method 2:
# s=set(l1)
# print(list(s))



