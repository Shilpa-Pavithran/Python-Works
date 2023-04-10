# Flow of control is used to control the programming flow. They are 3 types
# 1. Decision Making
# 2. Looping
# 3. Switching

''''Decision making is anticipation of conditions occurring while execution of the program and
 specifying actions taken according to the conditions.

# simply decision making method is used to run a code in a particular time based on a condition/decision.

There are few blocks used for decision making method: All these blocks executes boolean expression
* If block - works on the condition is True
* Else block - works on when If block statement is False else works
* Elif block - works on the condition is True
* Nested If block - in one if condition another if condition is used- its also works on the condition is True '''

#Syntax

# if condition: - for blocks colon : is must
#     code - indentation will be there
# elif condition:
#     code
# else: - no code for else

num=int(input('Enter num: '))
if num>50:
    print(num)
else:
    print('in else')

# Example:
FA=int(input('Enter fixed amount: '))
Withdraw=int(input("Enter the withdrawal amount:"))
if Withdraw<=FA:
    print(Withdraw, 'is debited from your a/c, and the remaining balance is: ', FA-Withdraw)
else:
    print('Insufficient Balance')