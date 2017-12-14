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

del fruit["lemon"]
print(fruit)

print(fruit.keys())

if "apple" in fruit:
    print("apple is in fruit")

for key in fruit:
    print("Key: {}".format(key))

fruit.clear
print("Printing empty fruit")
print(fruit)

