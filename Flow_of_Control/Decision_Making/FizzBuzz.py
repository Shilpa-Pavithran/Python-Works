# Program to print in the below condition
# divisble by 3 Fizz
# divisble by 5 Buzz
# divisble by 15 FizzBuzz

num=int(input("enter num to check: "))
if num%15==0:
    print("FizzBuzz")
elif num%5==0:
    print("Buzz")
else:
    print('Fizz')
