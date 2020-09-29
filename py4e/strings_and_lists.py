#words = 'His e-mail is q-lar@freecodecamp.org'
#pieces = words.split()
#parts = pieces[3].split('-')
#n = parts[1]
#print(n)

han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    #print('Line:',line)
    if line == '' :
        #print('Skip blank')
        continue
    wds = line.split()
    #print('Words:' ,wds)
    if len(wds) < 3 or wds[0] != 'From' :
        #print("Ignore")
        continue
    print(wds[2])