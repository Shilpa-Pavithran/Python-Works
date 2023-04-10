'''' Input and Output data
print()- used to display a message in console
input() - To read a value from the console
'''

print('hello')
# input('Enter a name')
print('Good Morning')

# coma , is used to seperate the var name and strings in the print()
Company='Luminar Technolab'
Location='Cochin'
print('The company name is', Company, '\nand the location is', Location) # Here  coma, \n are keywords
print(Company,'\n',Location) # here there is no strings used only two variables. hence we put the \n in separate quotes.

# Using Input() to input data
comp=input() # can use input data without using the string but when a new user comes they don't understand what to enter
comp1=input('Enter company name')
loc=input('Enter Location')
print('The company name is', comp1, '\nand the location is', loc)

# example
num1=150
num2=200
print(num1+num2)
sum=num1+num2
print(sum)

# input data always take the value as string. To change to other data type . We use Type Conversion method
int() , float(), str(), bool()
n1=input("enter number")
print(type(n1))
n2=int(input('Enter num1'))
n3=int(input("enter num2"))
sum=n2+n3
print(type(n2))
print(sum)