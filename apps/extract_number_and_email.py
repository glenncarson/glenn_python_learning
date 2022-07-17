# import re

# # grab most emails. may need to edit for odd
# email_regex = re.compile('\w+[.-_]?\w*?[.-_]?\w*?@.*?\.com|edu|org|net|gov|us|io|co|me',re.I)
# email_regex.findall('andy_samberg@gmail.com or glenn.a.carson@gmail.com')


# # book's solution
# # [a-zA-Z0-9._%+-]+ covers everuything up to the @, which is nice
# # vs. \w+[.-_]?\w*?[.-_]?\w*? and is technically not 100% coverage 
# re.compile('[a-zA-Z0-9._%+-]+')


# book solution
import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})       # dot-something
    )''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []
# print phoneRegex.findall(text)
# print '\n'
# print emailRegex.findall(text)
# print '\n'

for groups in phoneRegex.findall(text):
    # print groups[1]
    # print groups[3]
    # print groups[5]
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])
# print '\n'
# print matches

# print '\n'

if matches:
    pyperclip.copy(', '.join(matches))
    print ', '.join(matches)
else:
    print "No matches were found. Are you sure you copied target text to clipboard?"

# test text:
# Sentence 1 with (530)-400-4813.
# Sentence 2 with glenn.a.carson@gmail.com.
# Sentence 3 with 916-606-4628 and also rosa.elizabeth.johnson@gmail.com.
# User: (530)-753-6279


# other project ideas
# Clean up dates in different date formats 
# (such as 3/14/2019, 03-14-2019, and 2015/3/19) 
# by replacing them with dates in a single, standard format.