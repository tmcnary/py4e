word = "bananana"
i = word.find("na")
print(i)

print('exercise 6.5')
str = 'X-DSPAM-Confidence: 0.8475'
print(str)
ipos = str.find(':')
print(ipos)
piece = str[ipos+1:]
print(piece)
value = float(piece)
print(value)