# part 1
with open("input-day07.txt") as input:
    positions = [int(p) for p in list(input)[0].split(",")]
    start = min(positions)
    stop = max(positions)

    min_fuel = None
    min_pos = None

    for target_position in range(start, stop):
        fuel = sum([abs(p - target_position) for p in positions])

        if min_fuel is None or fuel <= min_fuel:
            min_fuel = fuel
            min_pos = target_position

    print(min_fuel)


# part 2
with open("input-day07.txt") as input:
    positions = [int(p) for p in list(input)[0].split(",")]
    start = min(positions)
    stop = max(positions)

    min_fuel = None
    min_pos = None

    for target_position in range(start, stop):
        fuel = sum([(pow(abs(p - target_position), 2) + abs(p - target_position)) / 2 for p in positions])

        if min_fuel is None or fuel <= min_fuel:
            min_fuel = fuel
            min_pos = target_position

    print(int(min_fuel))