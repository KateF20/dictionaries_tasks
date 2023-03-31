dictionary = [input() for i in range(int(input()))] # get input number of lines of a dict
words = [input().lower() for i in range(int(input()))] # get input number of lines of lowered words to search

# dict comprehension to make a dict from a list, splitting each element by ': ' and lowering the keys
my_dict = {i.split(': ')[0].lower(): i.split(': ')[1] for i in dictionary}

for word in words: # print a value from the dict
    print(my_dict[word] if word in my_dict.keys() else 'Не найдено')