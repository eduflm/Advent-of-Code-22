import math

alphabet = "abcdefghijklmnopqrstuvwxyz"

priority_dictionary = {}
current_priority = 1
for c in alphabet:
    priority_dictionary[c] = current_priority
    priority_dictionary[str.upper(c)] = current_priority + 26
    current_priority += 1

file = open("C:\Dev\Advent-of-Code-22\day-3\input.txt", "r")

current_sum = 0

for line in file:
    clean_line = line.replace("\n", "")
    middle_point = math.floor(len(clean_line) / 2)
    
    first_part = set(clean_line[0:middle_point])
    second_part = set(clean_line[middle_point:])

    intersection = first_part.intersection(second_part)

    current_sum += priority_dictionary[intersection.pop()]

print(current_sum)