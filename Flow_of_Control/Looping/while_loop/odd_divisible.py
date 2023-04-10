# print a program of odd number and that are divisible by 3 using user input value

initial=int(input('Enter initial value: '))
final=int(input('Enter final value: '))
while initial<=final:
    if initial%2!=0 and initial%3==0:
        print(initial)
    initial+=1
