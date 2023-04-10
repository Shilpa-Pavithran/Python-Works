# List method :

l1=[5,2,69,80,5.5,4,3]
print(l1)
l1.pop()  # it will remove last elements from the list
print(l1)
l1.remove(80)  # used to remove any single element from the list
l1.append(250)  # used to add single element to a list
l1.extend([9,1,7])  # used to add iterable objects into the list.can add any iterable object(tuples, sets, dictionaries)
print(l1)
l1.sort()  # used to sort the elements in ascending order
print(l1)
print('minimum element',l1[0])
print('maximum element',l1[-1])
l1.reverse()  # reverses the current sorting order of the elements.
print(l1)
print(min(l1))  # in-built function of min
print(max(l1))  # in-built function of max
print(sum(l1))  # in-built function of sum
l2=[5,4,6]
l2.copy()  # Returns a copy of the list
print(l2)
l2.count(0)  # Returns the number of elements with the specified value
print(l2)

# Join two list or can use extend method
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
