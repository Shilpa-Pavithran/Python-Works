# Switching
'switching are mainly used to control the looping statement. switching are not blocks they are statements'
# We use 2 switching statements which are:

# 1. break
# 2. continue

''' Break statement - is used to stop or break a loop. It will stop the current and upcoming iterations.
  Continue statement - it will only stop current iteration and process the remaining iteration. '''

# Else in For Loop
'''The else keyword in a for loop specifies a block of code to be executed when the loop is finished'''
# Eg:-
for x in range(6):
  print(x)
else:
  print("Finally finished!")

# Pass Statement

# for loops cannot be empty, but if you for some reason have a for loop with no content,
# put in the pass statement to avoid getting an error.

# Eg:
for x in [0, 1, 2]:
    pass

# having an empty for loop like this, would raise an error without the pass statement
