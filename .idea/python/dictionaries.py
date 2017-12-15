fruit = {
    "orange": "a sweet, orange, citrus fruit",
    "apple": "good for making cider",
    "lemon": "a sour, yellow citrus fruit",
    "grape": "a small, sweet fruit growing in bunches",
    "lime": "a sour, green citrus fruit",
    "apple": "round and crunchy"
}

print(fruit)
print(fruit["lemon"])

fruit["pear"] = "an odd shaped apple"
print(fruit)

fruit["pear"] = "great with tequila"
print(fruit)

exist = fruit.get("lemon", "we do not have a lemon")
print(exist)

does_not_exist = fruit.get("tomato", "we do not have a tomato")
print(does_not_exist)

print(fruit.keys())

if "apple" in fruit:
    print("apple is in fruit")

for key in fruit:
    print("Key: {}".format(key))

ordered_keys = list(fruit.keys())
ordered_keys.sort()

for f in ordered_keys:
    print(f + " - " + fruit[f])

print("\nFruit keys:")
print(fruit.keys())

print("\nFruit values:")
print(fruit.values())

print("\nFruit items:")
print(fruit.items())

f_tuple = tuple(fruit.items())
print("\nPrinting tuple:")
print(f_tuple)

print("\n")

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)

print("\ndictionary from tuple:")
print(dict(f_tuple))


del fruit["lemon"]
print("\nFruits after deleting lemon:")
print(fruit)

# please, note we have to use the parenthesis,
# as otherwise a method does not work.
fruit.clear()
print("\nPrinting empty fruit")
print(fruit)

