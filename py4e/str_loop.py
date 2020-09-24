string = input('input your string: ')
for itvar in string :
    print(itvar)

fruit = 'banana'
index = 0
while index <len(fruit) :
    letter = fruit[index]
    print(index, letter)
    index = index + 1

#pattern in loop
word = input("enter a word: ")
count = 0
for letter in word :
    if letter == 'a' :
        count = count + 1
print(count)