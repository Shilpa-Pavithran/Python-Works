# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
# In Python, we are allowed to extract the values back into variables. This is called "unpacking":

t=(2,3,4)
a,b,c=t
print(a)
print(c)

# swapping numbers using tuple unpacking method
num1=7
num2=9
num1,num2=num2,num1
print(num1)
print(num2)

# Using Asterisk*
"""If the number of variables is less than the number of values, you can add an * to the variable name 
and the values will be assigned to the variable as a list:"""

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)



