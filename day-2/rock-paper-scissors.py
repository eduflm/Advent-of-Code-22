# Rock - 1 point
# Paper - 2 points
# Scissors - 3 points

# Win - 6 points
# Draw - 3 points
# Lost - 0 points

# A - X - Rock
# B - Y - Paper
# C - Z - Scissors

# for each line
#   check if I win, draw or lost
#   check which move i made
#   sum points

file = open("C:\Dev\Advent-of-Code-22\day-2\input.txt", "r")

strategy_guide = {
    "X" : "C",
    "Y" : "A",
    "Z" : "B"
}

points_per_move = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

equivalents = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

current_sum = 0

for line in file:
    play = line.replace("\n", "").split(" ")
    current_sum += points_per_move[play[1]]
    # If is a victory
    if strategy_guide[play[1]] == play[0]:
        current_sum += 6
    # elif is a draw
    elif equivalents[play[0]] == play[1]:
        current_sum += 3

print(current_sum)