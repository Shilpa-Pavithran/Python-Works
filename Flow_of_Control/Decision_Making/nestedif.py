# num=int(input("Enter num: "))
# if num>0: # nested if comese in one if with another if- works based on true statement
#     if num>5:
#         print(num)
#     else:
#         print('in else')
# else:
#     print('Out')

num=int(input("Enter num: "))
if num>0 and num>5: # or we can use if with logical operator
        print(num)
else:
        print('in else')

