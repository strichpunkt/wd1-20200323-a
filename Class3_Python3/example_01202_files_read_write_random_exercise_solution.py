# write a list with the ingredients salad, orange, mango
# choose randomly an ingredient, and write it to a file called "random_fruit.txt"
import random

food_list = ["salad", "orange", "mango"]

python_choice = random.choice(food_list)

with open("random_fruit.txt", "w") as f:
    f.write(python_choice)