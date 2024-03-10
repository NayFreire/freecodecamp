# EXEMPLE 1 -------------------------------------------------------------
list = [False, False, False]

count = 0
if [x for x in list if x]: #verify if the list is empty. If will only be false if the list is empty
    count += 1

print(count)

# ------------------------------------------------------------------------

# EXEMPLE 2 --------------------------------------------------------------
numbers = [1, 2, 3, 4, 5, 6, 7]

new_list = [number + 1 for number in numbers if number % 2 == 0]

print(new_list)

# ------------------------------------------------------------------------

# EXEMPLE 3 --------------------------------------------------------------
square = [number ** 2 for number in range(10)]
print(square)

# ------------------------------------------------------------------------

# EXEMPLE 4 --------------------------------------------------------------
names = ['Alice', 'Bob', 'Charlie']
ages = [30, 25, 35]
people = [{'name': name, 'age': age} for name, age in zip(names, ages)]
print(people)

# ------------------------------------------------------------------------