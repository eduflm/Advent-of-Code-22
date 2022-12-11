file = open("C:\Dev\Advent-of-Code-22\day-4\input.txt", "r")

overlaps = 0

for line in file:
    elfs_assignments = line.replace('\n', '').split(',')
    first_elf = elfs_assignments[0].split('-')
    first_elf_set = set(i for i in range(int(first_elf[0]), int(first_elf[1]) + 1))

    second_elf = elfs_assignments[1].split('-')
    second_elf_set = set(i for i in range(int(second_elf[0]), int(second_elf[1]) + 1))

    if (first_elf_set.issubset(second_elf_set) or second_elf_set.issubset(first_elf_set)):
        overlaps += 1

print(overlaps)