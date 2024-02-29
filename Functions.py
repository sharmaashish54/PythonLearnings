#average values 2 and 5 in args, but are overridden if passed as on line 5
def average(a=2,b=5):
    print('average is ',(a+b)/2)

average(10,18)

# passing n number of numbers as tuples using * - single * means tuple while two stars ** means Dictionary
def averageOfNumbers(*numbers):
    sum = 0
    print(type(numbers))
    for i in numbers:
        sum+=i
        print(sum)
    print('averge is', sum/len(numbers))

averageOfNumbers(10,20,304,201,401)

