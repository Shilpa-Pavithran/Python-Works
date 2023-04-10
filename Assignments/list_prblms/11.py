# 11.write a python program to find the third largest number from given list of numbers.

largest = {"first": 0, "second": 0, "third": 0}
lst = [12, 45, 2, 41, 31, 10, 8, 6, 4]
for number in lst:
    if number > largest["first"]:
        largest["third"] = largest["second"]
        largest["second"] = largest["first"]
        largest["first"] = number
    elif number > largest["second"]:
        largest["third"] = largest["second"]
        largest["second"] = number
    elif number > largest["third"]:
        largest["third"] = number

print(largest)
print(largest["third"])

# method 2
l1=[20,63,32,54,89,10]
x=sorted(l1)
print('sorted list:',x)
print('Third largest number:',x[-3])
