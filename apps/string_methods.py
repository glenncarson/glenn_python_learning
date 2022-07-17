# # print ("hi this is Alice's friend")
# # print ('hi this is Alice\'s friend')
# # print ('backslash print test \\')
# # print 'this is a test \n hi'
# from curses.ascii import isdigit


# print r'string test \ hi'

# spam = 'Hello from Kauai. This place is nice and sunny'
# print spam
# print spam[1:3]
# print range(0,5)

# name = 'Glenn'
# number = 29
# print 'Hi my name is %s and I am %s years old' % (name,number)

# 'abc'.isupper()
# 'Abc'[0].isupper()
# ' '.isspace()
# # 4.isalnum()
# # note there are many .is*** methods isalnum, islower, isdigit, etc.

# while True:
#     print('Enter your age')
#     age = input() #raw_input forces everything to be a string
#     if type(age) == int:
#         break
#     else:
#         print('Passwords can only have letters and numbers.')

name1 = 'jersey'
name2 = 'jersey 2'
','.join([name1,name2])

# split(' ') and split '\n' allow you to pull text or data from weird strings
# instead of always using split, use partition when you want to keep that word!
vcf_path = '/locus/home/gcarson/JIRA/CPAE-999/bait_testing/output/CONDITION1/AT12345/XE12345/cnv.vcf'
vcf_path.split('/XE')
vcf_path.partition('/XE')[2]

# print "hello".rjust(10) #add padding with spaces
# print "hello".center(40,'*') #add padding with spaces


def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, ' ') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)



picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
print picnicItems.items()
def printDictTable(dict,width):
    print 'PICNIC ITEMS'.center(width,"*")
    for key, value in picnicItems.items():
        print key.ljust((width-4)) + str(value).rjust((4))
printDictTable(picnicItems,20)
printDictTable(picnicItems,36)

print "The monkey went to the table         ".strip()


print "The monkey went to the table         ".strip().strip('table')
spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam.strip('ampS')
chr(37)
ord('a')
ord('\xc9')
import pyperclip