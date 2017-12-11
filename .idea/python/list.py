# ipAddress = input("Please enter an IP address: ")
# print("Number of segments {}".format(ipAddress.count(".")))
#
# parrot_list = ["non pinin", "no more", "a stiff", "berets of live"]
#
# parrot_list.append("A Norwegian Blue")
#
# for state in parrot_list:
#     print("This parrot is " + state)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
original_numbers = numbers

if original_numbers == numbers:
    print("Original numbers equal to numbers")
else:
    print("Original numbers not equal to numbers")

print("Numbers list: {}".format(numbers))

numbers_sort = numbers.sort()

print("Numbers.sort: {}".format(numbers))

numbers_in_order = sorted(numbers)

print("Numbers sorted: {}".format(numbers_in_order))

print(numbers_in_order)

if numbers == numbers_in_order:
    print("The list are equal")
else:
    print("The lists are not equal")







