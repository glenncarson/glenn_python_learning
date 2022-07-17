#! python
import pyperclip
print "Usage: Copy desired text to reformat to the clipboard before running this script."

input_text = pyperclip.paste().split('\n')
print ("-"*30).center(40) + '\n'
new_text = ""
for i in input_text:
    print "* " + i# + '\n'
    new_text += "* " + i# + '\n'
print "\n" + ("-"*30).center(40)
pyperclip.copy(new_text)

