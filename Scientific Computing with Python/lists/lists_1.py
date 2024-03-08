numbers = [x for x in range(0, 50)]

evens = lambda even: even % 2 == 0
even_numbers = list(filter(evens, numbers))

odds = lambda odd: odd % 2 != 0
odd_numbers = list(filter(odds, numbers))

print(even_numbers, '\n', odd_numbers, 2 % 2 == 0)