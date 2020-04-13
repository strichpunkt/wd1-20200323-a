# coding=utf-8
# create a for loop, which iterates through all meals
# print the meal and the price each iteration
shoppinglist = {"bread": 100, "butter": 90, "avocado": 10}

for food in ["bread", "butter", "avocado"]:
    print(food, shoppinglist[food])


# Extra: sum up all prices and print the total shopping cost
price = sum(shoppinglist.values())
print(price)


# oder

total = 0
for food, price in shoppinglist.items():
    total+=price
print(total)