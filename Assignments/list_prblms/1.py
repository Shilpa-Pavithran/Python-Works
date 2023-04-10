# 1. Write a program to seperate negative and positive numbers from a given list? (accept input from the user)

n=int(input('Enter the total no.of list elements: '))
l1=[]
for i in range(1,n+1):
    num=int(input('enter the value:'))
    l1.append(num)
print(l1)
l2=[]
l3=[]
for j in range(n):
    if l1[j]>0:
        l2.append(l1[j])
    else:
        l3.append(l1[j])
print('List of positive numbers: ',l2)
print("list of negative numbers: ", l3)
