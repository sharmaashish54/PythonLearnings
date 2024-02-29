tableOf = int(input("Enter number for which you want to print table :"))
for i in range(12):
    if(i == 10):
        # skip the entire loop and come out
        break;
    print(tableOf,'X',i+1,'=',tableOf*(i+1))  


for i in range(12):
    if(i == 10):
        # skip the iteration and continue
        print('skipped for ',i)
        continue;
    print(tableOf,'X',i,'=',tableOf*(i))  