a_list = []

#  index  0  1  2  3
#        -4 -3 -2 -1
b_list = [1, 2, 3, 4]
print(a_list)
print(b_list)

# reference
# print a_list[0]  # IndexError, because has no elements

print(b_list[-1])  # 4  -1 ist der letzte index
b_list[1] = 10     # wir greifen auf das element mit dem index 1 zu --> ist in dem fall 2 und überschreiben den index mit der zahl 10
print(b_list)

c_list = ["fist", 1000, False, [1, 2, 3]]
print(c_list)
c_list[0] = 10
c_list[1] = "thousand"
c_list[2] = 0
c_list[3] = None
print(c_list)

# strongly typed -> C, C++, JAVA, C#
# dynamically typed -> Python, JavaScript
