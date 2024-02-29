marks = [20,19,16,18,17,19,17]
# enumerate gives you index as well along with values
for index, mark in enumerate(marks):
    # print(index,'value',mark)
    if(mark < 18):
        print(f'B at position : {index+1}')
    else:
        print('A')

# start value can also be changed for enumerate
print('after index 3')
for index, mark in enumerate(marks, start=4):
    # print(index,'value',mark)
    if(mark < 18):
        print(f'B at position : {index+1}')
    else:
        print('A')
