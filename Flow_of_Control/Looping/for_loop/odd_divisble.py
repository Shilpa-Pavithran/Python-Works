#write a program to print odd number with divisible by 3 in user given range

initial=int(input('Enter initial range: '))
final=int(input('Enter final range: '))
for i in range(initial,final+1):
    if i%2!=0 and i%3==0:
        print(i)