import shelve


path = "../../Presentations/Shelve/"
file_name = path + "ShelfTest"

#with shelve.open(file_name) as fruit:
fruit = shelve.open(file_name)
# fruit["orange"] = "a sweet, orange, citrus fruit"
# fruit["apple"] = "good for making cider"
# fruit["lemon"] = "a sour, yellow citrus fruit"
# fruit["grape"] = "a small, sweet fruit growing in bunches"
# fruit["lime"] = "a sour, green citrus fruit"
#
# print(fruit["lemon"])
# print(fruit["grape"])
#
# fruit["lime"] = "good with tequila"

# for snack in fruit:
#     print(snack + ": " + fruit[snack])
#
# while True:
#     dict_key = input("Please, enter a fruit: ")
#     if dict_key == "fruit":
#         break
#
#     if dict_key in fruit:
#         decription = fruit[dict_key]
#         print(decription)
#     else:
#         print("We do not have a " + dict_key)

# print("=" * 40)
#
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
#
# for f in ordered_keys:
#     print(f + " - " + fruit[f])

for v in fruit.values():
    print(v)

print(fruit.values())

for f in fruit.items():
    print(f)

print(fruit.items())


fruit.close()

# print(fruit)