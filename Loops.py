#If elif else loop
age = int(input("Enter your age : "))
if age>18:
    print('you can drive as your age is :',age,"years old.")
elif age<18:
    print('you cannot drive since you are less than 18 years old')
else:
    print('not a valid age')


# for loops

name = 'Ashish'

for i in name:
    print(i,end=',')

colorList = {'orange','red','blue','white'}

if 'orange' in colorList:
    print("Yes")
else:
    print('No')    

for color in colorList:
    print(color)

for x in range(21):
    print(x)

for x in range(1,21):
    print(x)

# skip by 2 
for x in range(1,21,2):
    print(x)

# while loop
z=1
while(z<21):
    print(z)
    z= z+1
count =5
while(count>0):
    print(count)
    count= count-1