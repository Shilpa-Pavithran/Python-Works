d={'name':'shilpa','age':25,'place':'kannur'}
print(d)
d1=d["place"] # can directly call the value using square brackets
print(d1)
d1=d.get('name') # to get the particular value
print(d1)
print(d.keys()) # return a list of all the keys in the dictionary.
d['year']=2023
print(d.keys())
print(d.values()) # return a list of all the values in the dictionary.
d['name']='Nidhin'
print(d.values())
d["year"]=2018
print(d) # change the value of a specific item by referring to its key name:
print(d.items()) # return each item in a dictionary, as tuples in a list
d.copy() # Make a copy of a dictionary
print(d)

# The update() method will update the dictionary with the items from the given argument.
d.update({'color':'red'})
print(d)
# method 2 directly adding the key:values using square braces
d['phn']=2578568
print(d)

# Remove items in dictionary
d.pop('age') # removes the item with the specified key name:
print(d)
d.popitem() # removes the last inserted item
print(d)
del d["year"] # del particular item from dict
print(d)
d.clear() # removes all the items from the dict
print(d)
del d # delete the entire dictionary and occurs error
print(d)
