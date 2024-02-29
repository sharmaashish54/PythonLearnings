# Empty set can be created as below
set = set()
print(type(set))
# this is empty dictionary
dict = {}
print(type(dict))
# no duplicates are allowed in set, order is 
set = {1,1,2,4,5,6,5,2,3,90}
print(type(set))
print(set)

set1 = {90,98,76,12}
# symmetric difference means the values which are not common in two sets
set2 = set.symmetric_difference(set1)
print(set2)
# Return the difference of two or more sets as a new set.
# (i.e. all elements that are in this set but not the others.) - A-B
set3 = set.difference(set2)
print(set)