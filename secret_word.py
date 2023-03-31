scrypted = input()
letters = [input().split(': ') for i in range(int(input()))] # get all the symbols in a list
letters_dict = {i[1]: i[0] for i in letters} # make a dict where letters are keys and their frequencies are values
scrypted_dict = {i: scrypted.count(i) for i in scrypted} # make the same list but for the word

# replace letters from the scrypted word with letters from the given dictionary
for i in scrypted:
    x = str(scrypted_dict[i])
    print(letters_dict[x], end='')