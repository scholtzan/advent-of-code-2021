# part 1
with open("input-day02.txt") as input:
    horizontal = 0
    depth = 0

    for line in input:
        instr = line.split(" ")
        direction = instr[0]
        distance = int(instr[1])

        if direction == "forward":
            horizontal += distance
        elif direction == "down":
            depth += distance
        elif direction == "up":
            depth -= distance
        else:
            print("unknown instruction")

    print(horizontal * depth)

# part 2
with open("input-day02.txt") as input:
    horizontal = 0
    depth = 0
    aim = 0

    for line in input:
        instr = line.split(" ")
        direction = instr[0]
        distance = int(instr[1])

        if direction == "forward":
            horizontal += distance
            depth += aim * distance
        elif direction == "down":
            aim += distance
        elif direction == "up":
            aim -= distance
        else:
            print("unknown instruction")

    print(horizontal * depth)