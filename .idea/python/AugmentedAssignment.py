
number = "9,223,372,036,854,775,807"
cleanedNumber = ""

for i in range(0, len(number)):
    if number[i] in "0123456789":
        cleanedNumber += number[i]

newNumber = int(cleanedNumber)
print("The number is {} ".format(newNumber))

x = 23
x += 1
print(x)

x -= 4
print(x)

x **= 2
print(x)