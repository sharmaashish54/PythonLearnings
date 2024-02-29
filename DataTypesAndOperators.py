a = 10
a+=1
b=2
for i in range(0,10):
    b+=1;
print(a)
print(b)
print(a+b)
print(type(a))
print(type(a+b))
c = 'Ashish'
d = 'Sharma'
print(c+' '+d)
print(type(c+' '+d))
#Float and int can be added
e= 1.1
print(type(e))
# implicit type casting
print(a+e)

multiLineStr = """my name is ashish
this is my first exercise in python and 
now i have learnt how to write multiline strings"""

print(multiLineStr)

for character in multiLineStr:
    print(character)

'''list of above data type 
can be combined in a list - multiline comments
list can be modified- adding or removing the elements can be done'''
list = [a,b,c,d,e]
print(type(list))
print(list)
list.append('10')
print(list)

#operators
print(a+b)#add
print(a-b)#sub
print(a*b)#multiply
print(a/b)#divide
print(a//b)#divide result without decimal value
print(a**b)#a to the power b
print(a%b)#modulus or reminder


