# Задание 1

elements_list = ['a', 6, 34.45, 2, 'Toyota']

elements_list.pop(2)

print(len(elements_list))

elements_list.reverse()

new_list = [True, 21.34]

elements_list += new_list

print(elements_list)

# Задание 2

first_list = [1, 3, 5]
second_list = [2, 4, 6]

# first_list += second_list
first_list = first_list.__add__(second_list)

print(first_list)
