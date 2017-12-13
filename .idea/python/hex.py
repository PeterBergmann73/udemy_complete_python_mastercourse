# for i in range(17):
#     print("{0:>2} in hex is {0:>02x}".format(i))
#
# x = 0x20
# y = 0x0a
#
# print(x)
# print(y)
# print(x * y)
#
# print(0b101010)

power_lower_bound = 0

power_upper_bound = 15

powers = []

power_range = list(range(power_upper_bound, -1, -1))

for power in power_range:
    powers.append(2 ** power)

print(powers)

lower_bound = 2 ** power_lower_bound
upper_bound = 2 ** (power_upper_bound + 1) - 1

num = int(input("Please, enter number between {} and {}: ".format(lower_bound, upper_bound)))

while num < lower_bound or num > upper_bound:
    num = int(print("Number is outside of the bounds, please, enter another number: "))

remainer = num
binary = []

for power in powers:
    binary.append(remainer // power)
    remainer = remainer % power

print("Number {} in binary format is :".format(num))

for val in binary:
    print(val, end="")


