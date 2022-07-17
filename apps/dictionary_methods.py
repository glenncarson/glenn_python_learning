# glenn_dict = {}

# glenn_dict['language'] = 'Python'
# glenn_dict['transit'] = 'Bike'
# glenn_dict['vegetable'] = 'Cucumber'


# type(glenn_dict.items())
# # .items(), .values(). .keys() all useful for loops

import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for char in message:
    count.setdefault(char,0) # keep default. add character to dict with value 0 if not existing
    count[char] = count[char] + 1 # add value of 1 for every observation

pprint.pprint(count)

