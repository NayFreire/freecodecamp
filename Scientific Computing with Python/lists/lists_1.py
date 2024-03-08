numbers = [x for x in range(0, 100)]

evens = lambda even: even % 2 == 0
even_numbers = sorted(numbers, key=evens)

odds = lambda odd: odd % 2 != 0
odd_numbers = sorted(numbers, key=odds)

print(even_numbers, '\n', odd_numbers, 2 % 2 == 0)