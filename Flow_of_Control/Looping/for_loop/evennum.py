#program to print even number of user input range

num1=int(input('Enter initial range: '))
num2=int(input('Enter final range: '))
for i in range(num1,num2+1):
    if i%2==0:
        print(i)