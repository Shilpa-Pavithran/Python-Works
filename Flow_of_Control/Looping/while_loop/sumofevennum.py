# print sum of even number with user input range

num1=int(input('Enter initial range: '))
num2=int(input('Enter final range: '))
sum=0
while num1<=num2:
    if num1%2==0:
        sum=sum+num1
    num1=num1+1
print(sum)
