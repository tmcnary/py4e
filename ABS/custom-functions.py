def greetings(name) :
    print('Hello ' + name)

greetings('Alice')
greetings('Bob')
greetings('my darlin\'')

def plusOne(number):
    return number + 1

newNumber = plusOne(5)
print(newNumber)


# def salutations(name = 'null') :
def salutations(name = None) :
    name = str(input('Enter a name: '))
    print('Hello ' + name)
salutations()