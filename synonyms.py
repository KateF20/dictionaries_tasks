synonyms = [input().split() for i in range(int(input()))] # get list of word pairs
dict_syn = {key: value for key, value in synonyms} # create a dict with one synonym as a key and another as a value

word = input()
if word in dict_syn.keys(): # if the word given is the first in the pair
    print(dict_syn[word])
elif word in dict_syn.values(): # if it is the second
    key = [k for k, v in dict_syn.items() if v == word] # get the key for a value
    print(*key)