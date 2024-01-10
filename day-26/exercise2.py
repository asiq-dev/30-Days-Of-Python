# 2) Use a defaultdict to store a count for each character that appears in a given string. Print the most common character in this dictionary.

from collections import defaultdict

s = "onomatopoeia"
letter_count = defaultdict(int)

for character in s:
    letter_count[character] += 1

most_common_character = max(letter_count, key=lambda key: letter_count[key])

print(most_common_character)