# print 1 to 50 divisible by 10 and even numbers in a list using list comprehension

new=[i for i in range(1,51) if i%10==0 and i%2==0]
print(new)

# method without using list comprehension
new1=[]
for i in range(1,51):
    if i%10==0 and i%2==0:
        new1.append(i)
print(new1)