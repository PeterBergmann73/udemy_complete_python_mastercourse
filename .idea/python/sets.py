farm_animals = {"sheep", "cow", "hen"}

print(farm_animals)

for animal in farm_animals:
    print(animal)

print("=" * 40)

wild_animals = set(["lion", "tiger", "panther", "elephant"])

for animal in wild_animals:
    print(animal)

farm_animals.add("horse")
wild_animals.add("horse")

print(farm_animals)
print(wild_animals)

empty_set = set()
empty_set2 = {}
# empty_set2.add("a")

even = set(range(0, 40, 2))
print(even)

squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(squares)
print(len(squares))

print(even.union(squares))
print(len(even.union(squares)))

print(even.intersection(squares))
print(len(even.intersection(squares)))

print(sorted(even))
print(sorted(squares))

print("even minus squares")
print(sorted(even - squares))
print(sorted(even.difference(squares)))

print("squares minus even")
print(squares.difference(even))
print(squares - even)

print("=" * 40)
print("symmetric even minus squares")
print(sorted(even.symmetric_difference(squares)))

print("symmetric squares minus even")
print(sorted(squares.symmetric_difference(even)))

squares.discard(4)
squares.remove(16)
squares.discard(8) # no error, does nothing
print(squares)

try:
    squares.remove(8)
except KeyError:
    print("The item 8 is not a member of the set")

print("=" * 40)

even = set(range(0, 40, 2))
print(even)

squares = set([4, 6, 16])
print(squares)

if squares.issubset(even):
    print("squares is a subset of even")

if even.issuperset(squares):
    print("even is a superset of squares")

even = frozenset(range(0, 100, 2))
print(even)

# even.add(3)
# print(even)
