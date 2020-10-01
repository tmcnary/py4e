#py4e dictionary exercise
print('dictionary exercise')

fname = input('Enterfile: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w  in wds:
        di[w] = di.get(w,0) + 1
    #print(lin)
   # wds = lin.split()
    #print(wds)
   # for w in wds:
   #     print('**',w,di.get(w,'not in dict'))
   #     if w in di :
   #         di[w] = di[w] + 1
    #        print('**EXISTING**')
    #    else:
    #        di[w] = 1
    #        print('**NEW**')
    #    print(w,di[w])
largest = -1
theword = None
for k,v in di.items() :
    if v > largest :
        largest = v
        theword = k
print('the most common word is: ',theword,', with a count of: ',largest)