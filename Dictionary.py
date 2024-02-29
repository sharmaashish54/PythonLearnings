dict = {1222340:"Marsh&Mcllenan",33118:"Syntel",11029276:"Accenture",120140:"Sapient"}

print(dict)
print(type(dict))

print(dict.keys)

for k in dict.keys():
    print(k)
for v in dict.values():
    print(v)

for k in dict.keys():
    print(f"The valus in dict for key {k} is {dict[k]}")

dict2 = {22121988: "Google", 11022017:"Microsoft"}

dict.update(dict2)
print(dict)

dict3 = dict
# to remove an item from dict:
dict2.pop(22121988)
print(dict2)
# to remove last item from dict:
dict2.popitem()
print(dict2)

print('dict3',dict3)

del dict3
print(dict3)