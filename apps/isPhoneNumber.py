# https://automatetheboringstuff.com/2e/chapter7/
# regex examples above

# compile creates the search string-form
# findall(string) or .search(string).group() returns hits

import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # doesn't work with .groups()
phoneNumRegex.search('My number is 415-555-4242 and also 415-555-4244').group() #all
phoneNumRegex.search('My number is 415-555-4242 and also 415-555-4244').group(1) #first group
phoneNumRegex.search('My number is 415-555-4242 and also 415-555-4244').groups()

area_code, main_number = phoneNumRegex.search('My number is 415-555-4242 and also 415-555-4244').groups()
phoneNumRegex.findall('My number is 415-555-4242 and also 415-555-4244')#.groups()

area_code, main_number 

# searchobject = re.compile(search string format)
# searchobject.search(string_to_search).group() --> shows first hit

phoneNumRegex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
# escape to search for () in a regex
# \.  \^  \$  \*  \+  \?  \{  \}  \[  \]  \\  \|  \(  \) all are special characters in regex
phoneNumRegex.search('My number is (415)-555-4242 and also 415-555-4244').group(1)

# can regex only return the first match?
dog = re.compile(r'(\(Parentheses\))').search('(Parentheses) oh yeah').group()
dog
re.compile(r'Batman|Tina Fey').findall('Tina Fey is Batman')  #.search('Tina Fey is Batman').findall()

re.compile('Bat(man|mobile|copter|bat)').search('Batman and his Batcopter found Batbat alive and safe').group()
# pretty interesting way to use a prefix and then multiple options to finish

# optional search keys in the middle of a word
batRegex = re.compile(r'(B|b)at(wo)?man')
batRegex.search('This is Batwoman').group()
batRegex.search('This is batwoman').group()


# find numbers with or without an area code 
# 530-400-4813, (530)-400-4813, (530) 400-4813
phone_number = re.compile('(\()?\d\d\d(\))??(-)?( )?(\d\d\d-\d\d\d\d)')
phone_number.search('My number is (415)-555-4242').group()

re.compile('\d*a').search('54321a').group() # optional (look for a number of any length) ending letter a
re.compile('\d+a').search('54321a').group() # look for a number of any length ending in letter a
re.compile('\d+a').search('54321') == None # is True
# re.compile('{\d}5').search('54321') #.group() ## 
re.compile(r'(43){2}').search('43435').group() # search for a blcok that repeats a certain number of times
re.compile(r'(43){,2}').search('434343435').group() # match up to 2 matches
re.compile(r'(43){2,4}?').search('434343435').group() # distinct use of ? to do a 'lazy' search. unrelated to optional char


phoneNumRegex = re.compile('\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex.findall('My number is 415-555-4242 and also 415-555-4244')
# finall acts different if there are any groups. if returns each group, but not the whole

xmasRegex = re.compile('\d+\s\w+') # number, space, unit
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')

# can make own character class
xmasRegex = re.compile('[aeiouAEIOU]') # number, space, unit 
# or conversely xmasRegex = re.compile('[^aeiouAEIOU]')
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
# manual method, which is not as good!

re.compile('^Hello').search('Hello mister').group()
re.compile('Hello$').search('mister Hello').group()

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
nameRegex.search('First Name: Al Last Name: Sweigart').group(1) #to get first name
# .* is really useful to pull any character up to any number of times it happens

print ('Serve the public trust.\nProtect the innocent.\nUphold the law.')
re.compile('.*').search('Serve the public trust. \nProtect the innocent. \nUphold the law.').group()
re.compile('.*',re.DOTALL).search('Serve the public trust. \nProtect the innocent. \nUphold the law.').group()

# substitution instead of search
re.compile('Agent\s\w+').sub('CENSORED','Agent Alice gave the secret documents to Agent Bob.')
re.compile(r'Agent\s(\w)\w+').sub(r'\1****','Agent Alice gave the secret documents to Agent Bob.')
# the raw string r'' is important for this in this case above! so not in compile, but in sub


# re.compile(r'Agent (\w)\w*').sub(r'\1****', 'Agent Alice told Agent Carol that Agent')

# def isPhoneNumber(text):
#     if len(text) != 12:
#          return False
#     for i in range(0, 3):
#         if not text[i].isnumeric():
#              return False
#     if text[3] != '-':
#          return False
#     for i in range(4, 7):
#         if not text[i].isnumeric():
#              return False
#     if text[7] != '-':
#          return False
#     for i in range(8, 12):
#         if not text[i].isnumeric():
#              return False
#     return True
# print('Is 415-555-4242 a phone number?')
# print(isPhoneNumber('415-555-4242'))
# print('Is Moshi moshi a phone number?')
# print(isPhoneNumber('Moshi moshi')) 