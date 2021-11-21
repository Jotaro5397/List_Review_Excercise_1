# Excercise 3
a_list = [3, 4, 6, 12]

print("\033[1m", 3)

a_list.reverse()

print(a_list)

a_list = [3, 4, 6, 12]

multiplied_list = [element * 3 for element in a_list]

print(multiplied_list)

a_list = [3, 4, 6, 12]
even_list = []

for num in a_list:
    if (num % 2 ) == 0:
        even_list.append(True)
    else:
        even_list.append(False)

print(even_list)