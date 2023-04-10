# A loop statement allows us to execute a statement or group of statements multiple times.

# Types in looping
# 1. For_loop
# 2. While_loop

# syntax for loop
# for - keyword , variable, in-keyword, range function(initial, final, increment): colon used for blocks

# final range
for i in range(5): # here we didn't provide the initial value, hence Variable consider 0 as default value.
    print('hello') # also we didn't provide increment value hence it will consider as 1. Each loop is called iteration

for i in range(5): # no initial value and increment value and print i as 0 as initial and increment with 1
    print(i,'Hi')

# initial final range
for i in range(5,10): # here 5 is initial value and 10 is final value.
    print(i,'Hello World')

# initial final increment range
for i in range(1,8,2): # 1 is initial, 8 is final and 2 is increment value
    print(i,'Good Morning')

# Example programs
# print 1 to 10
for i in range(1,11):
    print(i)
# print 10 to 1
for i in range(10,0,-1):
    print(i)
# print 2,4,6,8
for i in range(2,9,2):
    print(i)