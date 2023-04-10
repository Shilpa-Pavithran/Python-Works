l=[10,20,30,10,10,20,30,40,50,40,70]
count={}
for i in l:
    if i not in count:
        count.update({i:1})
    else:
        val=count[i]
        val+=1
        count.update({i:val})
print(count)