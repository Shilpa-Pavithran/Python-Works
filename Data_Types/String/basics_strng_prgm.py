# String - Sequence of characters, digits, or symbols—always treated as text. Enclosed with quotes. Eg: 'Hi', "+1-999"

# String_programming

st1='Luminar Technolab'
print(st1)
# to iterate each element in string -using for loop method
for i in st1:
    print(i)

# To find a count of character in string
st2='Good Morning'
count=0
for i in st2:
    if i=='o':
        count=count+1
print(count)

# Find a program to check user input element present in the string
s='Hello Everyone'
find=input('Enter a element to check: ')
for i in s:
    if i == find:
        print('present')
        break
else:
    print('not present')

# other method- using membership keyword in/not in

if find in s: # the variable Find must be single element then only we can execute this method. without using for loop
    print('present')
else:
    print('not present')

# Find the count of vowels and consonant
str1 = input('Enter a string: ')
count = 0
for i in str1:
    if i in 'aeiou':
         count = count+1
print('count of vowels:', count)
#     if i not in 'aeiou':
#         count=count+1
# print('count of consonants:',count)

