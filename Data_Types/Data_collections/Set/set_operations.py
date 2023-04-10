s1={1,2,3,4,5}
s2={3,4,5,6,7,8}

# Union - Total elements from both the set
print(s1.union(s2))

# intersection  - set of common elements
print(s1.intersection(s2))

# difference - difference between the sets. that is s1-s2
print(s1.difference(s2))
print(s2.difference(s1))

# Symmetric difference - it will remove the common elements and print the remaining elements from the sets
print(s1.symmetric_difference(s2))