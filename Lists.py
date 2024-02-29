list = ['abc',1,2,'def','ashish',8]
print(type(list))
print(list)

list2 = [i for i in range(10)]
print(list2)

print('1 to 8 number :',list2[1:8])
# Filter our for index 1 to 8 and then skip by 2
print('1 to 8 number skipping 2:',list2[1:8:2])
# Filter our for index 1 to 8 and then skip by 3
print('1 to 8 number skipping 2:',list2[1:8:3])

list = [i*i for i in range(10) if i%2==0]
print(list)


# methods:
list = [12,323,124,546,74432,12]
list.reverse()
print(list)
# print(list.count())
print(list.count(12))
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.sort()
print(list)
list.extend(list2)
print(list)

newList = list + list2
newList.sort()
newList.append(90)
print(newList)