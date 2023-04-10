# print sum of even number with user input range

num1=int(input('Enter initial range:'))
num2=int(input('Enter final range: '))
sum=0
for i in range(num1,num2+1): #2+4+6+8+10
    if i%2==0:
        sum=sum+i
print(sum)