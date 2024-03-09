#sort words by length

words = ['thing', 'help', 'programming', 'apple', 'cost', 'apartment', 'die', 'school']

words_length = lambda word: len(word)
print(words_length)

sorted_words = sorted(words, key=words_length)

print(sorted_words)
