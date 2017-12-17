import shelve


path = "../../Presentations/Shelve/"
file_name = path + "ShelfTest"

#with shelve.open(file_name) as fruit:
fruit = shelve.open(file_name)
fruit["orange"] = "a sweet, orange, citrus fruit"
fruit["apple"] = "good for making cider"
fruit["lemon"] = "a sour, yellow citrus fruit"
fruit["grape"] = "a small, sweet fruit growing in bunches"
fruit["lime"] = "a sour, green citrus fruit"

print(fruit["lemon"])
print(fruit["grape"])

fruit.close()

print(fruit)