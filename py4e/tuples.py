d = dict()
d['quincy'] = 1
d['beau'] = 5
d['kris'] = 9
print(type(d))
print(d)
for (name,number) in d.items():
    print(number, name)

print('**End of first lesson** \n')

dictionary = dict()
dictionary['a'] = 10
dictionary['b'] = 1
dictionary['c'] = 22
print(dictionary)
print(dictionary.items())
print(sorted(dictionary.items()))

print('**End of second lesson** \n')

file = open('clown.txt')
counts = dict()
for line in file:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, value in counts.items() :
    newtuple = (value, key)
    lst.append(newtuple)

lst = sorted(lst, reverse=True)

for value, key in lst[:10] :
    print(key, value)
#simplified function
print(sorted([ (value,key) for key,value in counts.items()], reverse=True))

print('**End of third lesson** \n')

filename = input('Enter file name: ')
if len(filename) < 1 : filename = 'clown.txt'
file = open(filename)

dictionary =  dict()
for line in file:
    line = line.rstrip()
    words = line.split()
    for w in words:
        # idiom: retrieve/create/update counter
        dictionary[w] = dictionary.get(w,0) + 1
print(dictionary)

temp = list()
for key,value in dictionary.items():
    print(key,value)
    newtuple = (value,key)
    temp.append(newtuple)

print('Flipped', temp)
temp = sorted(temp, reverse=True)
print('sorted',temp[:5])

for value,key in temp[:5] :
    print(key,value)
