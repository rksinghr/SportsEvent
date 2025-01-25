import pyotp
import pytz
from datetime import datetime

utc = pytz.utc
# Initialize the TOTP object with a secret key
# totp = pyotp.TOTP('JBSWY3DPEHPK3PXP')  # example secret key
seck = pyotp.random_base32()
totp = pyotp.TOTP(seck, interval=90)
otp = totp.now()
print(otp)

otp = input("Enter the OTP: ")

totp = pyotp.TOTP(seck, interval=90)
otp = totp.now()
print(otp)

valid_date = datetime.now(utc)
print(valid_date)
otp = input("Enter the OTP: ")
# Verify the OTP
if totp.verify(otp):
    print("Authentication successful")
else:
    print("Invalid OTP")
