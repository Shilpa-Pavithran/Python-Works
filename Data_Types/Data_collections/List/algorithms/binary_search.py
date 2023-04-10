#Binary search
''''Binary Search is a searching algorithm used in a sorted array by repeatedly dividing the search interval in half.
The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(Log n).
'''

# in this example count of iteration is low.

l=[1,5,2,3,8,9,10]
def binary_search(e): #e=8
    count=0
    flag=0
    l.sort() #[1,2,3,5,8,9,10]
    low=0  # low=0
    upper=len(l)-1 #upper=6
    while low<=upper: #0<=6
        count+=1
        midindex=(low+upper)//2 # 0+6//2=3 --> 5 will be the middleelement
        if e==l[midindex]: #8==5
            flag=1
            break
        elif e>l[midindex]: # 8>5
            low=midindex+1 #3+1=4
        elif e<l[midindex]:
            upper=midindex-1
    if flag==1:
        print('Present')
    else:
        print("Not Present")
    print('Count',count)
binary_search(8)
binary_search(15)