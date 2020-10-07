import re
file = open('mbox-short.txt')
for line in file:
    line = line.rstrip()
    if re.search('^From:', line) :
        print(line)
print('**End of lesson**\n')

x = 'my 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]', x)
print(y)
print('**End of lesson**\n')



s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)
print('**End of lesson**\n')

file = open('mbox-short.txt')
numlist = list()
for line in file:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))