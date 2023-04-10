# Print a program which is divisible by 5 and even
s={4,5,6,7,8,9,10,15,16,20,30}
new=set()
for i in s:
    if i%2==0 and i%5==0:
        new.add(i)
print(new)