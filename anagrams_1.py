words = [input() for i in range(2)] # get input words in a list
word_1, word_2 = {}, {} # set dicts when key is a letter and value is frequency of the letter in the word

# add a letter to the dict and when it appears again, increase the value
for elem in words[0]:
    word_1[elem] = word_1.get(elem, 0) + 1

for elem in words[1]:
    word_2[elem] = word_2.get(elem, 0) + 1

# if both dicts have the same key/value pairs, print 'YES', otherwise print 'NO' using list comprehensions
print('YES' if word_1 == word_2 else 'NO')