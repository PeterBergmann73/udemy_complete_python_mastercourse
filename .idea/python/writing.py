cities = ["Adelaide", "Alice Spring", "Darwin", "Melbourne", "Sydney"]

path = "../../Presentations/FileIO/"

cities_file = "cities.txt"

# with open(path, 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file)

# with open(path, 'r') as city_file:
#     for city in city_file:
#         cities.append(city.strip('\n'))
#
# print(cities)
#
# for city in cities:
#     print(city)

# imelda = "More Mayhem", "Imelda MAy", "2011" , (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")
# )
#
# with open(path + "imelda3.txt", 'w') as imelda_file:
#     print(imelda, file=imelda_file)

with open(path + "imelda3.txt", 'r') as imelda_file:
    contents = imelda_file.readline()

imelda = eval(contents)

print(imelda)
title, artist, year, tracks = imelda

print(title)
print(artist)
print(year)


