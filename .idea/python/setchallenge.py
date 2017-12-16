vowels = frozenset("aeiou")

input_string = input("Please, enter your string ")

letter_set = set(input_string)

charachters = letter_set.difference(vowels)

print(charachters)