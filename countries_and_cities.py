to_dict = [input().split(' ') for i in range(int(input()))] # get the list of countries and cities in them
cities = [input() for i in range(int(input()))] # get the list of cities

countries = {}
for i in range(len(to_dict)): # iterate over all countries
    for elem in to_dict[i][1:]: # iterate over all elements of one country
        countries[elem] = to_dict[i][0] # assign a country to each city; city is a key and country is a value

print('\n'.join(countries[city] for city in cities)) # print value by a key