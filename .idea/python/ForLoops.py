for i in range(1,3):
    print("i is: {}".format(i))

number = "9,223,372,036,854,775,807"

for i in range(0, len(number)):
    print(number[i])

cleanedNumber = ""
for i in range(0, len(number)):
    if number[i] in "0123456789":
        cleanedNumber = cleanedNumber + number[i]

newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))

cleanedNumber = ""

for char in number:
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char

newNumber = int(cleanedNumber)

print("The number is {}".format(newNumber))

for state in ["not pinin", "no more", "a stiff", "bereft of life"]:
    print("This parrot is " + state)

for i in range(0, 100, 5):
    print("is is {}".format(i))