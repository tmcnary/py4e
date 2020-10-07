spam = 0
while spam < 50:
    print("Hello, world!")
    spam = spam + 1
print('**end of lesson**\n')

name = ''
while True :
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')
print('**end of lesson**\n')

spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))
print('**end of lesson**\n')