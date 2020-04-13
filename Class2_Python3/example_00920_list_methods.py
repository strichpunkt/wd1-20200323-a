a_list = []
b_list = [1, 2, 3, 4]

# append
b_list.append(5)  # wir fügen ein element am ende der liste hinzu
print(b_list)  # [1, 2, 3, 4, 5]

# remove
b_list.remove(3)
print(b_list)  # [1, 2, 4, 5]
# extend - muss eine liste sein. ist iterierbar.
b_list.extend([0, 77, 99])
print(b_list)  # [1, 2, 4, 5, 0, 77, 99]
b_list += [100, 101]  # wie ein concat
print(b_list)  # [1, 2, 4, 5, 0, 77, 99, 100, 101]

c_list = [0]
c_list.append(1)
c_list.extend([2])
print(c_list)


c_list.append([3, 4, 5])
print(c_list)      # [0, 1, 2, [3, 4, 5]]

c_list.extend([3, 4, 5])
print(c_list)      # [0, 1, 2, [3, 4, 5], 3, 4, 5]