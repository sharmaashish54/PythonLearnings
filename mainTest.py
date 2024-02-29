import Hello

# this is printed two times, one from here and one from Hello class
# Hello.hello()

# to avoid this 

print(__name__)
if __name__ == "--main--":
    Hello.hello()