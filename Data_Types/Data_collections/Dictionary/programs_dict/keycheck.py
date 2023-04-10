d={1:100,2:200,3:300,4:400,5:500}
key=int(input('Enter the key: '))
if key in d.keys():
    print('present')
else:
    print('Not present')

# method2:
key=int(input('Enter the key: '))
if key in d:
    print('present')
else:
    print('Not present')

# Value check
value=int(input('Enter the value: '))
if value in d.values():
    print('present')
else:
    print('Not present')
