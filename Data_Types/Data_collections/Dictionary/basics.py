'''Dictionaries are used to store data values in key:value pairs.

* A dictionary is a collection which is ordered
* changeable/mutable
* Do not allow duplicates in keys but values - support duplicates
* Dictionaries are written with curly brackets, and have keys and values:
* Heterogeneous elements used (list,string,bool,int,float,tuple,set)
* unidexed
* support nesting

'''

d={'name':'anu',1:2.5,'age':23,'new':True,'color':["blue",'red'],(1,2):(2,3),2:{'value':25},3:{2,5}}
print(d)
print(type(d))

d1={'name':'anu','name':'arun'} # keys do not allow duplicates
print(d1)

d2={'name':'anu','new':'anu'}  # Values support duplication
print(d2)

# empty dict
d3={}
d4=dict()  # type constructor of dictionary is dict(), used to make a new dict
print(type(d3))
print(type(d4))