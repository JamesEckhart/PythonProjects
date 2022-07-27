#Declare variable and initialize it
f = 101
print(f)

#Global vs. local variables in fuctions
def someFunction():
    f = 'Testing 1...2...3...4...5...' #Local variable inside the function, assumes local scope
    print(f)

someFunction()

print(f) #global varable, local variable was destroyed!!
