name = input('Enter your name: ')
agestr = input('Enter your age: ')
age = int(agestr)
if name == 'Alice' :
    print('Hi, Alice')
elif age < 12:
    print('You are not Alice, Kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, imortal vampire!')
elif age > 100:
    print('You are not Alice, Granny.')
else:
    print('Who are you, anyway?')