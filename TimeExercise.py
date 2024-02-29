import time

print(time.localtime())

timestamp = time.strftime('%H:%M:%S')
print(timestamp)

hours = int(time.strftime('%H'))
minutes = int(time.strftime('%M'))
seconds = int(time.strftime('%S'))

print('time is :',hours, minutes, seconds)

name = input("Enter your name sir: ")

if (hours>=0 and hours <12):
    print('Good morning',name)
elif(hours>=12 and hours<17):
    print('Good Afternoon',name)
elif(hours>=17 and hours<21):
    print('Good Evening',name)
else:
    print('Good night',name)