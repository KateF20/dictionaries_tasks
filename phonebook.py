n = int(input())
# get list of lines with numbers and names
num_name = [input().split(' ') for i in range(n)]
names = [input().title() for i in range(int(input()))] # get list of all names to find in a phonebook

phone_book = {}
# make a dictionary where a name is a key and numbers are values; use get to set the first number and add to it another
for i in range(len(num_name)):
    key, value = num_name[i][1], num_name[i][0]
    phone_book[key] = phone_book.get(key, '') + ' ' + value

# print using list comprehensions
[print(phone_book[name].strip()) if name in phone_book else print('абонент не найден') for name in names]
