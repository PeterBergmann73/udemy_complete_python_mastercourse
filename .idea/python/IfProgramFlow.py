# name = input("Please, enter your name: ")
# age = int(input("How old are you, {0}? ".format(name)))
# print(age)
#
# if age >= 18:
#     print("You are old enough to vote")
# else:
#     print("Please, come back in {0} years".format(18 - age))

# print("Please guess a number between 1 and 10: ")
# guess = int(input())
#
# if guess != 5:
#     if guess < 5:
#         print("Please, guess higher")
#     else :
#         print("Please, guess lower")
#
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")


# age = int(input("How old are you? "))
#
# if 16 <= age <= 65:
#     print("Have a good day at work")
#
# if (age < 16) or (age > 65):
#     print("Enjoy your free time")

print(not False)

parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter not in parrot:
    print("I don't need that character")
else:
    print("Good")