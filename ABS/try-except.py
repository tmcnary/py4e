#error handling with try and except

def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))

print('**end of lesson**\n\n')

print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) < 0:
        print('There\'s no such thing as negative cats')
    elif int(numCats) >= 4:
        print('That\'s a lot of cats.')
    else:
        print('That\'s not that many cats.')
except ValueError:
    print('Please enter a number in digits.')
