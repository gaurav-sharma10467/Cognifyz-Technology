# Develop a Python function that validates
# whether a given string is a valid email
# address. Implement checks for the format,
# including the presence of an "@" symbol and
# a domain name

def validate_email(email):
    if('@' in email):
        print("This is a correct email you have entered")
    else:
        print("You have entered wrong email")

email=input("Enter Your email for validation:-")
print(validate_email(email))