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
three_batch_set = []
current_count = 1

for line in file:
    clean_line = line.replace("\n", "")
    three_batch_set.append(set(clean_line))
    if (current_count == 3): 
        intersection = three_batch_set[0].intersection(three_batch_set[1].intersection(three_batch_set[2]))
        current_sum += priority_dictionary[intersection.pop()]
        current_count = 0
        three_batch_set = []
    current_count += 1

print(current_sum)