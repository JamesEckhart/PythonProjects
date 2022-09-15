f = 101
print(f)

#Global vs. local variables in fuctions
def someFunction():
    global f #see global varaiable inside fuction!
    print (f)
    f = "changing global variable"

someFunction()
print(f) #global varable, local variable 'I am learning Python' was destroyed!!!
