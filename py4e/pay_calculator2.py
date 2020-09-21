print("Welcome to Pay Calculator")
def computepay(fhours, frate):
    print("In computepay", fhours, frate)
    if fhours > 40 :
        print("You've earned overtime pay")
        rpay = 40 * frate
        otpay = (fhours - 40) * (frate * 1.5)
        pay = rpay + otpay
        print("Your regular pay is:",rpay, "Your overtime pay is:",otpay)
    else:
        print("No overtime was earned")
        pay = fhours * frate
    print("Returning",pay)
    return pay

shours = input("Enter your hours: ")
srate = input("Enter your pay rate: ")
fhours = float(shours)
frate = float(srate)

xp = computepay(fhours, frate)
print("Your pay is:",xp)