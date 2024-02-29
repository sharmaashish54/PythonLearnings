# if input is atleast 3 characters long , remove the first letter 
# and append in last and append 3 random charcter in first and 
# last else reverse the string

str = input('Enter a string for generating code word: ')

def code(str):
    if len(str) >3:
        str = 'abc' + str[1:] +str[0] +'abc'
        return str
    else:
       return ''.join(reversed(str))

print(code(str))

# if length is less than 3 reverse the input else remove 
# 3 character from front and end and then remove the last 
# character and append in front.

str = input('Enter a word for decode :')
def decode(str):
    if len(str) >3:
        str = str[3:-3]
        str = str[-1] +str[0:-1]
        return str
    else:
       return ''.join(reversed(str))

try:
   print(decode(str))
except:
    print('wrong input')