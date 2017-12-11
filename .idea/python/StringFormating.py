age = 24
print("My age is " + str(age) + " years")

print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, and {3}".format(31, "January", "March", "May"))

#right and left aligning
for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {1:<4}".format(i, i**2, i ** 3))


print("January: {2}, February: {0}, March: {2}".format(28, 30, 31))


for i in range(1, 12):
    print("No. {} squared is {} and cubed is {:4}".format(i, i**2, i ** 3))