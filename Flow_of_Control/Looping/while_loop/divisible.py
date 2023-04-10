# print a program of divisible by 5 with user input range

initial=int(input('Enter initial range: '))
final=int(input('Enter final range: '))
while initial<=final:
    if initial%5==0:
        print(initial)
    initial+=1 # here we have put incrementation out of the if block because, when we provide increment inside if block
                # it will works only when the condition is true