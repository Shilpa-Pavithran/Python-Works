# print divisible by 5 using user inputs

initial=int(input("Enter initial range: "))
final=int(input("Enter final range: "))
for i in range(initial,final+1):
    if i%5==0:
        print(i)