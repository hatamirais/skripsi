import pyotp

base32secret = str('COVZJUEGCHTYXLW5')
print('Secret:', base32secret)

totp = pyotp.TOTP(base32secret)

otp = totp.now()

your_code = input('')
if your_code == otp:
    print("Valid")
else:
    print("Invalid")
    
# COVZ JUEG CHTY XLW5