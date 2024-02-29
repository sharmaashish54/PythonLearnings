a = input('enter a number :')

print(f'Table for number {a}')
try:
    for i in range(1,11):
        print(f'{a} X {i} = {int(a)*i}')
except:
    print("not a number, exception occurred")

print('End of table till 10')
# finally is always executed whether a function returns from try or except
try:
    num = int(input('enter a number'))
    a= [6,3]
    print(type(a))
    print(a[num])
except ValueError:
    print('Number entered is not an integer')
except IndexError:
    print('Index Error')
finally:
    print('I am always executed')

# custom error 
b = int(input('enter a value between 1 to 5'))
try:
    if (b > 5 or b<1):
        raise ValueError("not in range of 1 to 5.")
except ValueError:
    print('Not a valid number')