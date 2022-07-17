# ask via command line for message to translate
# handles most messages except for those with special characters, e.g. "'" within a word, like Alice's
message = raw_input('Please enter a message to translate into pig-latin ').split()

vowels = ['a','e','i','o','u']
punctuation = '!,.;:?'
def wordHasVowel(word):
    vowel_status = False
    for vowel_letter in vowels:
        if vowel_letter in word.lower():
            vowel_status = True
    return vowel_status
def isaAlpha(word):
    number_status = True
    if word.isalpha() == True:
        number_status = False
    return number_status

list_len = len(message)

for index in range(0,list_len):
    if isaAlpha(message[index]) == True:
        for char in punctuation:
            if message[index][-1] == char:
                message[index] = message[index][0:-1]
                if wordHasVowel(message[index]) == True:
                    while message[index][0].lower() not in vowels:
                        message[index] = message[index][1:] + message[index][0]
                    message[index] = message[index] + 'ay' + char
                if wordHasVowel(message[index]) == False:
                    message[index] = message[index][0:-1]+'ay' + char
    if isaAlpha(message[index]) == False:
        if wordHasVowel(message[index]) == True:
            while message[index][0].lower() not in vowels:
                message[index] = message[index][1:] + message[index][0]
            message[index] = message[index] + 'ay'
        if wordHasVowel(message[index]) == False:
            message[index] = message[index]+'ay'
print ' '.join(message)
            
