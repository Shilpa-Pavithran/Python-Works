s='hello hi hello hi hi luminar'
data=s.split()
print(data)
count={}
for i in data:
    if i not in count:
        count[i]=1
    else:
        val=count[i]
        val+=1
        count[i]=val
print(count)