# String slicing

fullName = 'Ashish Sharma'
print("First Name is :", fullName[0:6])
print("Last Name is :", fullName[7:])
print("second way to print First Name is :", fullName[:-6])
print("second way to print Last Name is :", fullName[-6:])

# print(fullName[-4:-2])

# str = 'Harry'
# print(str[-4:-2])

print(fullName.upper())
# String is immutable, every operation gives a new string.
# the above operation doesn't change the original string.
print(fullName)

str = '!!!@Ashish@!!!'
# rstrip will only remove the trailing ! and not the one's which are in front
print(str.rstrip('!'))

print(str.replace('!',''))
print(str.split("@"))

str2 = 'ashish Sharma is my name'

print(str2.capitalize())
print(str2.title())
print(str2.swapcase())
