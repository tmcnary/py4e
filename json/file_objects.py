#working with file objects

#opens the file with a context manager in read mode; variable is set afterward
with open('builder-api.json', 'r') as f:
    
    size_to_read = input('How many characters would you like to read:')
    f_contents = f.read(int(size_to_read))
    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(int(size_to_read))
    #for line in f:
     #   print(line, end='')

    #f_contents = f.readline()
    #print(f_contents)
#opens file with chosen mode and assigns it to a variable f files opened this way must be closed
#modes are r = read, w = write, r+ read and write
#f = open('builder-api.json', 'r')

#prints the name of the opened file
print(f.name)
#prints the mode of the opened file
print(f.mode)
#closes the file after opening
#f.close()