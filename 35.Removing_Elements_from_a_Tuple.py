my_tuple = (1, 2, 3, 4,5)

temp_list = list(my_tuple)
temp_list.remove(2)
my_tuple = tuple(temp_list)

print('Tuple after Removal:', my_tuple)