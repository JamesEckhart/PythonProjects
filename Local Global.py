#Declare a variable and initialize it
f = 101
print(f)

#Global vs. local variables in functions
def someFunction():
#global f
    f = 'testing 123'
    print(f)


someFunction()
print(f)