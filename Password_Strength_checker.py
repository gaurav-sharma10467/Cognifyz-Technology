# Create a Python function that evaluates
# the strength of a password entered by the
# user. Implement checks for factors such as
# length, presence of uppercase and
# lowercase letters, digits, and special
# characters.

import re

def password_strength_checker(password):
    strength=0
    remarks=""
    
    if len(password)>=8:
        strength+=1
    
    if re.search(r'[a-z]',password):
        strength+=1
    
    if re.search(r'[A-Z]',password):
        strength+=1
        
    if re.search(r'/d',password):
        strength+=1
    
    if re.search(r'@',password):
        strength+=1
    
    if strength==5:
        remarks="Strong password"
    elif strength>3:
        remarks="Moderate Password"
    else:
        remarks="Weak Password"
    
    return remarks

password=input("Enter your password")
print(password_strength_checker(password))