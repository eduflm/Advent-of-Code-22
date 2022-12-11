# Rock - 1 point
# Paper - 2 points
# Scissors - 3 points

# Win - 6 points
# Draw - 3 points
# Lost - 0 points

# A - X - Rock
# B - Y - Paper
# C - Z - Scissors

# Z - Win
# Y - Draw
# X - Lose

# for each line
#   check if I win, draw or lost
#   check which move i made
#   sum points


file = open("C:\Dev\Advent-of-Code-22\day-2\input.txt", "r")

strategy_guide = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}

opposite_strategy_guide = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}

equivalents = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

points_per_move = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}


current_sum = 0

for line in file:
    play = line.replace("\n", "").split(" ")
    if (play[1] == "Z"):
        current_sum += 6 + points_per_move[strategy_guide[play[0]]]
    elif (play[1] == "Y"):
        current_sum += 3 + points_per_move[equivalents[play[0]]]
    else:
        current_sum += points_per_move[opposite_strategy_guide[play[0]]]

print(current_sum)
