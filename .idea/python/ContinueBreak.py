# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
#
# for item in shopping_list:
#     if item == "spam":
#         print("I am ignoring: " + item)
#         continue
#
#     print ("Buy " + item)
#
# print("======")
#
# for item in shopping_list:
#     if item == "spam":
#         print("I am ignoring: " + item)
#         break
#
#     print ("Buy " + item)

meal = ["egg", "bacon", "spam", "sausages"]

nastyFoodItem = ""

for item in meal:
    if item == "spam":
        nastyFoodItem = item
        break
    else:
        print("I'll have a plate of that")

if nastyFoodItem == "spam":
    print("Found spam")
else:
    print("No spam found")