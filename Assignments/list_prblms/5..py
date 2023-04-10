# 5.Write a python program to print all even numbers from a given list

l=[26,97,15,48,74,63,16,20,35,9]
l1=[]
for i in l:
    if i%2==0:
        l1.append(i)
print("Even numbers: ",l1)