''' Tuples are used to store multiple items in a single variable.

*A tuple is a collection which is ordered , indexed and unchangeable/immutable.
* Tuples are written with round brackets.
* Heterogeneous elements are used like (list,tuple,set,dict,string,bool,int,float)
* allows duplicate
* nesting possible
* without round brackets we can use tuples '''

t=(1,2,3,4,[1,2,3],True,{1,2},'Hello',0.5,{23:25,20:24},1,2,3,4,(1,2,3))
print(type(t))
print(t)
tst=t[5]
print(tst) # support indexing
t1=2,3,4
print(t1)
print(type(t1))
t2=tuple() # tuple constructor - empty tuple

# To create a tuple with only one item, you have to add a comma after the item,
# otherwise Python will not recognize it as tuple.
tpl=('new',)
tpl2=95,
print(tpl)
print(type(tpl))
print(tpl2)
print(type(tpl2))

