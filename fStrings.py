firstname = 'Ashish'
lastname = 'Sharma'

print(f"my name is {firstname} {lastname}")

price = 2.999999

print(f"{price:.2f}")

# docstrings

def square(n):
    '''Takes the number and returns square of number'''
    print(n**2)

square(5)
print(square.__doc__)