#program to print even number of user input range

num1=int(input('Enter initial num1: '))
num2=int(input('Enter final num2: '))
while num1<=num2:
    if num1%2==0:
        print(num1)
    num1+=1