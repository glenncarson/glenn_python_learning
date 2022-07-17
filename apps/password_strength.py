# Write a function that uses regular expressions to make sure the password string it is passed is strong. 
# A strong password is defined as one that is at least eight characters long, 
# contains both uppercase and lowercase characters, and has at least one digit. 
# You may need to test the string against multiple regex patterns to validate its strength.

# 8 characters or more
# has uppercase and lowercase characters
# has at least 1 digit

import re

user_input_for_password = input('Enter a password with at least 8 characters, uppercase and lowercase letters, and at least 1 digit. ')

def determine_strength_of_password(password):
    # first rule: 8 or more of any char
    re.compile(r'(.){8,}').search(password).group()

    # second rule: has uppercase and lowercase characters
    try:
        re.compile(r'(.*)?([A-Z])(.*)?').search(password).group() # finds an uppercase letter
    except AttributeError:
        quit('Uppercase letter not found. Try a different password.')
    try:
        re.compile(r'(.*)?([a-z])(.*)?').search(password).group() # finds an uppercase letter
    except AttributeError:
        quit('Lowercase letter not found. Try a different password.')

    # third rule: has at least 1 digit
    try:
        re.compile(r'(.*)?([1-9])(.*)?').search(password).group()
    except AttributeError:
        quit('Password does not contain a number. Try a different password.')
    print('New password created.')

determine_strength_of_password(user_input_for_password)


# Regex Version of the strip() Method
# use groups with (\s*)(text)(\s*) and return middle group only...
