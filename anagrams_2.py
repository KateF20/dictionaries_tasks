import string

words = [input().lower().replace(' ', '').strip() for i in range(2)] # get two input words in a list
words_only = [word.translate(str.maketrans('', '', string.punctuation)) for word in words] # remove punctuation

word_1, word_2 = {}, {}

# add a letter to the dict and when it appears again, increase the value
for elem in words_only[0]:
    word_1[elem] = word_1.get(elem, 0) + 1

for elem in words_only[1]:
    word_2[elem] = word_2.get(elem, 0) + 1

# if both dicts have the same key/value pairs, print 'YES', otherwise print 'NO' using list comprehensions
print('YES' if word_1 == word_2 else 'NO')