# goal is to animate with *s
#     ********
#    ********
#   ********
#  ********
# ********
#  ********
#   ********
#    ********
#     ********

# something simlar to  for i in range[0,10]
# if __ print(" "), else, print("*")
# start with 5 spaces, then go down

# code for one way change
# spaces_base = 5
# stars_base = 10
# for i in range(0,12):
#     if i <= 5:
#         spaces = spaces_base - i 
#         print((" "*spaces)+"*"*stars_base)
#     if i > 5:
#         # for 6, want 1 space, so i - 5
#         spaces = i - spaces_base
#         print((" "*spaces)+"*"*stars_base)


import sys

number = raw_input('Enter an integer number for collatz function. ')

try:
    number = int(number)
except: ValueError('Not an integer)')

if isinstance(number,int) == False:
    quit('Number not an integer. Aborting.')

def collatz(number):
    number
    if number % 2 == 0:
        number = number/2
        print number
    elif number % 2 != 0:
        number = (number * 3) + 1
        print number
    return number

while number > 1:
    number = collatz(number)