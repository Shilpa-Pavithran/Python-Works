# program to print salary of employee above 55000 using tuple

employee=(('anu','dev',50000),('arun',"dev",57000),('nita',"tester",35000))
for i in employee:
    if i[2]>55000:
        print(i)

# print employee names who are developers
for i in employee:
    if i[1]=='dev':
        print(i[0])

# print job of employee who has less salary
for i in employee:
    if i[2]<50000:
        print(i[1])

# other method using list to get the output
sal=[]
for i in employee:
    sal.append(i[2])
min_sal=min(sal)
for i in employee:
    if i[2]==min_sal:
        print(i[1])


