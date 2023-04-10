# String rotation
# the last element should come in first and the frist element goes to the last. 2 element rotation

# Eg: hello- it should be - lohel

s='Morning'
print(s[-2:]+s[:-2])


# Adding a string to an empty string

n='pineapple'
new=""  # Empty string
for i in n:
    new=new+i
print(new)

# Eg: to print consonants of a string in an empty string
v='strawberry'
n1=''
for i in v:
    if i not in 'aeiou':
        n1=n1+i
print(n1)