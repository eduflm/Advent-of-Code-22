import sys

if __name__ == "__main__":
    
    file = open("C:\Dev\Advent-of-Code-22\Day-1\input.txt", "r")

    highest_sum = 0
    current_sum = 0
    
    for line in file:
        if line == "\n":
            if current_sum > highest_sum:
                highest_sum = current_sum
            current_sum = 0
            continue
        number = int(line.replace("\n", ""))
        current_sum += number 
    
    print(highest_sum)

