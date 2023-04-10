# it used to print the repeated elements in a string

v='malayalam'
data=''
for i in v:
    if i not in data:
        data=data+i
    else:
        print(i)

# to print first recursive element in a string
# s='pineapple'
# new=''
# for i in s:
#     if i not in new:
#         new=new+i
#     else:
#         print(i)
#         break

# to print last recursive element in a string
s='Good Morning'
new = ''
dup=''
for i in s:
    if i not in new:
        new = new + i
    else:
        dup=dup+i
print(dup)
print('last recursive',dup[-1])
print('second recrsive',dup[1])
print('First recursive',dup[0])