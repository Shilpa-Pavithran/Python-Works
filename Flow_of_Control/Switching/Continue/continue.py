# for loop using continue statement.
for i in range(5+1):
    if i==2:
        continue # it will only stop the current iteration and process the remaining iteration
    print(i)

# another eg:

for i in range(5+1):
    if i==2 or i==4:
        continue
    print(i)

# While loop examples with continue statement
i=1
while i<=5:
    if i==2:
        continue #Here we have to put the incrementation code after the while block, bcoz once contine works it will not iterate
    print(i)
    i+=1 # Hence we have to use the iteration before the continue statement

# correct method for while loop with continue statement
i=1
while i<=5:
    i=i+1
    if i==3:
        continue
    print(i)