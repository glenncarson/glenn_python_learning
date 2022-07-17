# # while True:
# #     print('Infinite loooooooooop')

# name = raw_input('Who are you? ')
# # input()
# if name != 'Joe':
#     continue
#     print('Not Joe')

# # name = raw_input()

# for letter in 'Python':
#     if letter == 'h':
#         continue
#     print 'Current letter is {}'.format(letter)

# for letter in 'Python':
#     if letter != 'h':
#         print 'Current letter is {}'.format(letter)

'''
continue statement rejects all the remaining statements
 in the current iteration of the loop and moves
  the control back to the top of the loop.
'''

for letter in 'Python':
    if letter == 'h':
        pass
        print('pass block!')
    print(letter)

# if P, print
# if h -> continue ...???