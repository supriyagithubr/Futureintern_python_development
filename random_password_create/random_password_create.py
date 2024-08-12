import random
import string
print("welcome your random password generator..")
def password_function():
    length = int(input("Enter the lenth of password you want:-"))
    lowerdata = string.ascii_lowercase
    uperdata = string.ascii_uppercase
    digitdata = string.digits
    symboldata = string.punctuation
    letterdata = string.ascii_letters
    # print(lowerdata)
    # print(uperdata)
    # print(digitdata)
    # print(symboldata)
    # print(letterdata)
    combine = lowerdata+uperdata+digitdata+symboldata+letterdata
    s = random.sample(combine,length)
    # print(s)
    password = "".join(s)
    print(password)
    password_function()
password_function()
