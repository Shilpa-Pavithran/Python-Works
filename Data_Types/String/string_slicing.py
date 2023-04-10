'''You can return a range of characters by using the slice syntax.
Specify the start index and the end index, separated by a colon, to return a part of the string.
'''

s='Good Evening'
print(s[2:9])
print(s[2:10:2])
print(s[5:2:-1])
print(s[:6])
print(s[:3:-1])
print(s[4:])
print(s[:])
print(s[::-1])


# Print a program of palindrome
new_str=input('Enter a string: ')
if new_str==new_str[::-1]:
    print(new_str,'is a palindrome')
else:
    print(new_str,'is not a palindrome')