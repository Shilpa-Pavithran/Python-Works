# print factorial of user input num

num=int(input('Enter num to check: '))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)