# Linear Search
'''Linear search is a simple and flexible algorithm for finding whether an element is present within a list or array.
 It sequentially examines each element of the list/ array..'''

# in this example count of iteration is high. Hence it is complexity program

l=[1,5,2,3,8,9,10]
def linear_search(e):
    count=0
    for i in l:
        count+=1
        if i==e:
            print('Present')
            break
    else:
        print('Not Present')
    print("count",count)
linear_search(8)
linear_search(15)

