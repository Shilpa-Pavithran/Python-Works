# Logical Operators - are used to combine conditional statements:

# and , - Returns True if both statements are true
print (3>2 and 19>9)
print(2>5 and 25>20)
'''' 
True and True = True
True and False= False
False and True= False
False and False= False
'''
# or - Returns True if one of the statements is true
''''
False and False = False
False and True = True
True and False = True
True and True = True
'''
print(5>9 or 4>1)

# not - Reverse the result, returns False if the result is true
'''' not True = False
    not False= True
'''
print(not(4>9))
print(not(5>2))
print(not(3>2 or 20>9))