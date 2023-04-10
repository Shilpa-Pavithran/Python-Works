# normal for loop to print i
for i in range(5):
    print(i)

# for loop with break statement
for i in range(5):
    if i==2:
        break # it will stop current and upcoming iteration, also exit from the loop
    print(i)

# Examples for understanding:

for i in range(5):
    for j in range(5):
        if i==3:
            break # here it will break the inner loop.To break the outer loop have to give it in outside the loop
    print(i)

for i in range(5):
    for j in range(5):
        if i==3:
            break # break the inner loop
    if i==3:
        break # break the outer loop
    print(i)
