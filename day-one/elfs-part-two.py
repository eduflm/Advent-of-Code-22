import sys

if __name__ == "__main__":
    
    file = open("C:\Dev\Advent-of-Code-22\day-one\input.txt", "r")

    sums = []

    current_sum = 0
    
    for line in file:
        if line == "\n":
            sums.append(current_sum)
            current_sum = 0
            continue
        number = int(line.replace("\n", ""))
        current_sum += number 
    
    sums.sort()
    top_three_sum = sums[-1] + sums[-2] + sums[-3]
    print(top_three_sum)

