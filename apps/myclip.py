#! python
'''
myclip.py a multi-clipboard program.
At any point, the pyperclip.copy() contents are changed by user using cmnd + c on computer
this takes in an argument when running the script and sets it as a variable
'''

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

import sys, pyperclip
if len(sys.argv) < 2:
     print ("Usage python myclip.py [keyphrase] - copy phrase text")
     sys.exit()
keyphrase = sys.argv[1]

if keyphrase in TEXT.keys():
        pyperclip.copy(TEXT[keyphrase])
        print "Text for " + keyphrase + " stored in clipboard."
else:
        print "There is no text for " + keyphrase

# this kind of code could be relvant if you write repetitive emails
# input "agree" or "upsell" or "sorry"
# output is prewritten text copiedto clipboard
