# Task 1
# take your shopping list, "bread", "butter", "chocolate"
# you are on a diet, and decide to remove "chocolate"
# print the list before and after removing
meals = ["bread", "butter", "chocolate"]
print(meals)
meals.remove("chocolate")
print(meals)

# Task 2
# after removing, you will add "beans" and "lenses"
# them to your list, and print your list
meals.append("beans")
meals.append("lenses")
print(meals)


# extra: try adding "peanut butter" and "banana" to the list by
# 1) adding (+)
# 2) extending
meals += ["peanut butter"]
print(meals)
meals.extend(["banana"])
print(meals)