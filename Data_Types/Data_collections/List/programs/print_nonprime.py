# program to print prime and non- prime
lst=[1,2,3,4,5,6,7,8,9,10]
prime=[]
nonprime=[]
for i in lst:
    for j in range(2,i):
        if i%j==0:
            nonprime.append(i)
            break
    else:
        prime.append(i)
print('prime', prime)
print('non-prime', nonprime)



