#Declare variable and initialize it
f = 101
print(f)

#Global vs. local variables in fuctions
def someFunction():
    f = 'I am learning Python'
    print(f)

someFunction()
print(f) #global varable, local variable 'I am learning Python' was destroyed!!!
