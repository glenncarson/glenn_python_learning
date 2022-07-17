cat = ['fat','gray','loud']
size = cat[0]

size, color, temperament = cat
# ^^ is nice for value unpacking from lists, tuples
# good for integration into pandas, i believe


for index, item in enumerate(cat):
    print index
    print item
list(enumerate(cat)).sort()


spam = ['apples', 'bananas', 'tofu', 'cats']
spam[-1]
output_string = ""
# apples, bananas, tofu, and cats
for i in spam:
    if i not in spam[-1]:
        output_string += i + ', '
    if i == spam[-1]:
        output_string += "and " + i
print(output_string)