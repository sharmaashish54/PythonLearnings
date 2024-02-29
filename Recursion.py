def factorial(n):
    if (n ==1 or n ==0):
        return 1
    else:
        return n*factorial(n-1)

number = int(input('Enter the number for which you want to calculate factorial'))
print(factorial(number))


def fibonacci(n):
    if (n==0 or n==1):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
    print(fibonacci(i))