#Booleans represent one of two values: True or False.
# True means 1
# False means 0
# When comparing two values, the expression is evaluated and Python returns the Boolean answer:

print(10 > 9)
print(10 == 9)
print(10 < 9)

# Print a message based on whether the condition is True or False:
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# The bool() function allows you to evaluate any value, and give you True or False in return,
print(bool("Hello"))
print(bool(15))

# Evaluate two variables:
x = "Hello"
y = 15

print(bool(x))
print(bool(y))