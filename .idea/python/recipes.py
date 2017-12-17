import shelve


path = "../../Presentations/Shelve/"
file_name = path + "recipes"

# blt = ["bacon", "lettuce", "tomato", "bread"]
# beans_on_toast = ["beans", "bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

# writeback - to allow for appending.
with shelve.open(file_name, writeback=True) as recipes:
    # recipes["blt"] = blt
    # recipes["beans_on_toast"] = beans_on_toast
    # recipes["scrambled_eggs"] = scrambled_eggs
    # recipes["pasta"] = pasta
    # recipes["soup"] = soup

    # recipes["blt"].append("butter")
    # recipes["pasta"].append("tomato")

    # append some values

    # temp_list = recipes["blt"]
    # temp_list.append("butter")
    # recipes["blt"] = temp_list
    #
    # temp_list = recipes["pasta"]
    # temp_list.append("tomato")
    # recipes["pasta"] = temp_list
    # recipes["soup"].append("croutons")

    recipes["soup"] = soup
    recipes.sync()
    soup.append("cream")

    for snack in recipes:
        print(snack, recipes[snack])