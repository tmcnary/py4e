fileHandle = open('mbox-short.txt')
print(fileHandle)

for i in fileHandle:
    ly  = i.rstrip()
    print(ly.upper())