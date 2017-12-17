path = "../../Presentations/FileIO/"

# file_name = "sample2.txt"
#
# with open(path + file_name, 'a') as write_file:
#     for i in range(2, 13):
#         for j in range(1, 13):
#             print("{0:2} times {1} is {2:<4}".format(j, i, i * j), file=write_file)

file_name2 = "sample3.txt"

with open(path + file_name2, 'a') as write_file:
    for i in range(2, 13):
        for j in range(1, 13):
            write_file.write("{0:2} times {1} is {2:<4}\n".format(j, i, i * j))
