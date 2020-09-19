print("Welcome to Pay Calculator")
shours = input("Enter your hours: ")
srate = input("Enter your pay rate: ")
try:
    fhours = float(shours)
    frate = float(srate)
except:
    print("Does not compute")
    quit("bye")

print(fhours, frate)
if fhours > 40 :
    print("You've earned overtime pay")
    rpay = 40 * frate
    otpay = (fhours - 40) * (frate * 1.5)
    print("Your regular pay is:",rpay, "Your overtime pay is:",otpay)
    pay = rpay + otpay
else:
    print("No overtime was earned")
    pay = fhours * frate
print("Your pay is:",pay)