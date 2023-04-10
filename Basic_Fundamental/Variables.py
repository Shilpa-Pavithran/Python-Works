'''' Variables - they are identifiers, used for assigning value, storing data
Variable naming rules: -
1. any character or set of characters are used to name a variable. Eg, a, b, C , num, student etc.
2. Do not use space in between the var name instead of space use Underscore
3. Can be snake notation - eg: Employee_no, Empl_name etc
4. Can be camel notation - eg: Num, myName etc
5. Do not use operator symbols
6. Do not use a number to name a variable-Can use number at the end or middle of a variable name. Eg:- Var1, St1_name
7. Do not use keywords or build-in keywords to name a variable.
8. Use unique name to variable or else content stored in var name will be changed once you update new value to that same var name
'''

# Temporary storage of data

num=40
num=95 # here we used same var name,Hence it will take the new value and store it in that name and old value removed.
print(num)

#Multiple assignment
a=b=c=100
c,d=10,20

# dynamicaly typed lang Eg:
new=5. # without specifying the data type we can directly assign the value
new1=False
print(type(new))
print(type(new1))

# Case sensitive
A=10
a=265 # python is a case-sensitive lang. hence it will treat each var separately
print(A)
print(a)

Num=10
NUM=25
NuM=6
nUM=8
nuM=9
Num1=80