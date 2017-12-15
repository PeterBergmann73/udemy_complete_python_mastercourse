locations = {
    0: "Computer",
    1: "Road",
    2: "Hill",
    3: "Building",
    4: "Valley",
    5: "Forest"
}

# the notation is a bit misleading
# this is the list of the exits from a given location
exits = {
    0: {"Q": 0},
    1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
    2: {"N": 5, "Q": 0},
    3: {"W": 1, "Q": 0},
    4: {"N": 1, "W": 2, "Q": 0},
    5: {"W": 2, "S": 1, "Q": 0}
}

vocabulary = {
    "QUIT": "Q",
    "NORTH": "N",
    "SOUTH": "S",
    "EAST": "E",
    "WEST": "W"
}

# print(locations[0].split())
# print(loca)

loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exists are " + availableExits + " : ").upper()
    print()
    # Parse the user input, using our vocabulary dictionary if necessary
    if len(direction) > 1:  # more than one letter, so check vocab
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break

    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")
