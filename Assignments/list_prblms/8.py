# 8. ['www.zframez.com', 'www.wikipedia.org','www.asp.net','www.abcd.in']
# write a program to print website suffixes (com,org,net,in) from this list.

l1= ['www.zframez.com', 'www.wikipedia.org','www.asp.net','www.abcd.in']
for i in l1:
    print(i)
    new = i.find('.',4)
    print(i[new:])
