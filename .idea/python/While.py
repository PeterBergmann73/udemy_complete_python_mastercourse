# for i in range(10):
#     print("i is now {}".format(i))
#
# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1

import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a nuber between 1 and {}: ".format(highest))
guess = 0

while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    if guess > answer:
        print("Please guess lower: ")
    elif guess < answer:
        print("Please guess higher: ")
    else:
        print("You guessed correctly")

