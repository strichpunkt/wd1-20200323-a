# write a list with the ingredients salad, orange, mango
# choose one element of the list
# and write it to a file called "fruit.txt"
fruit_list = ["salad", "orange", "mango"]
chosen_fruit = fruit_list[1]
with open("fruit.txt", "w") as f:
    f.write(chosen_fruit)