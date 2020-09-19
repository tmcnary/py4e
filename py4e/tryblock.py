# Conditional Structures Try Block
temp = input("Enter Temp in F: ") # asks user for temp to convert
cel = 0
try:    
    fahr = float(temp)   
    cel = (fahr - 32.0) *5.0 / 9.0
except:
    fahr > 212
    print('It\'s too hot')

if fahr < 211:
    print(cel)
else:
    print('enter numbers only')