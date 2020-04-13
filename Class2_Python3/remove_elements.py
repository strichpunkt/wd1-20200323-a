a_list = [1,2,3,3,3,4,5,6]

#while 3 in a_list:
#    a_list.remove(3)
#print(a_list)


# list comprehension
b_list = [n for n in a_list if n != 3]
print(b_list)

