# Method 1 - using Temporary memory - but the best methods are 2 & 3 because not using extra memory
num1=int(input('Enter num1: '))
num2=int(input('Enter num2: '))
print('Before swapping num1=',num1)
print('Before swapping num2=',num2)
num=num1
num1=num2
num2=num
print('After swapping num1=',num1)
print('After swapping num2=',num2)

# Method 2 - using Tuple unpacking
num1=int(input('Enter num1: '))
num2=int(input('Enter num2: '))
print('Before swapping num1=',num1)
print('Before swapping num2=',num2)
num1,num2=num2,num1
print('After swapping num1=',num1)
print('After swapping num2=',num2)

# Method 1 - using arithemtic operator
num1=int(input('Enter num1: '))
num2=int(input('Enter num2: '))
print('Before swapping num1=',num1)
print('Before swapping num2=',num2)
num1=num1+num2 #
num2=num1-num2
num1=num1-num2
print('After swapping num1=',num1)
print('After swapping num2=',num2)
