# shopping_ist = ["milk", "eggs", "pasta", "bananas", "meat", "waffles"]
# for item in shopping_ist:
#     if item == "meat":
#         continue
#
#     print("Please, buy " + item)

meal = ["eggs", "milk", "spam", "bread"]

for item in meal:
    if item == "spam":
        nasty_food_item = item
        break

else:
    nasty_food_item = ''
    print("I'll have a plate of that")

if nasty_food_item == "spam":
    print("Can't I have anything else?")

for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break

for i in range(20):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)

for i in range(20):
    if i % 2 != 0 and i % 5 != 0:
        print(i)
