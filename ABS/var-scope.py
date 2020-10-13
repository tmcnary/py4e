spam = 42 #global variable

def eggs():
    spam = 42 #local variable
    print(spam)

print('some code here.')

def spam2():
    print(eggs)

eggs = 42
spam2()