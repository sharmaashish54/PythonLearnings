# cannot be changed once declared- TUPLES are immutable , stings are immutable, lists are mutable
tup = (1,5,10,17,5,12,5,10,5)
print(tup)
print(type(tup))

# positive indexing and negative indexing is same as list -1 means length-1

if 5 in tup:
    print('yes')
else:
    print('No')    

res = tup.count(5)
print(res)

res = tup.index(5)
print(res)
# slicing
res = tup.index(5,4,8)
print('sliced',res)


''' Convert a tup to a list and perform modification to 
the list and again covert it to tuple'''
list = list(tup)
list.append(20)
list.append(78)

tup = tuple(list)

print('tuple',tup)