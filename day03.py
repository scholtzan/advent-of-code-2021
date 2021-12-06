# part 1
with open("input-day03.txt") as input:
    total_lines = 0
    counts = []

    for line in input:
        total_lines += 1
        if counts == []:
            counts = [0] * len(line[:-1])
        
        for i in range(0, len(line[:-1])):
            counts[i] += int(line[i])

    most_common = ['1' if i > total_lines / 2 else '0' for i in counts]
    least_common = ['1' if i < total_lines / 2 else '0' for i in counts]

    gamma_rate = int("".join(most_common), 2)
    epsilon_rate = int("".join(least_common), 2)

    print(gamma_rate * epsilon_rate)

# part 2
def get_rating(numbers, most_common = True):
    for i in range(0, len(numbers[0])):
        # print(numbers)
        count = 0
        total_numbers = len(numbers)

        for num in numbers:
            count += int(num[i])

        if most_common:
            numbers = [num for num in numbers if num[i] == ('1' if count >= total_numbers / 2 else '0')]
        else:
            numbers = [num for num in numbers if num[i] == ('1' if count < total_numbers / 2 else '0')]

        if len(numbers) == 1:
            break


    rate = int("".join(numbers[0]), 2)
    return rate

with open("input-day03.txt") as input:
    numbers = [line[:-1] for line in input]

    oxygen = get_rating(numbers.copy())
    co2 = get_rating(numbers.copy(), False)
    print(oxygen * co2)
