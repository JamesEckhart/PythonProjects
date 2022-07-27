f = 100;
print(f)

#Global vs. Local variables in functions
def someFunction():
    global f
    print(f)
    f = "changing global variable"

someFunction()
print(f)