import shelve

path = "../../Presentations/Shelve/"
file_name = path + "book"

books = shelve.open(file_name)

books["recipes"] = {
    "blt": ["bacon", "lettuce", "tomato", "bread"],
    "beans_on_toast": ["beans", "bread"],
    "scrambled_eggs": ["eggs", "butter", "milk"],
    "soup": ["tin of soup"],
    "pasta": ["pasts", "cheese"]
}

books["maintenance"] = {
    "stuck": ["oil"],
    "loose": ["gaffer tape"]
}

print(books["recipes"])
# print(books["recipes"]["scrambled_eggs"])
#
# print(books["maintenance"]["loose"])

books.close()
