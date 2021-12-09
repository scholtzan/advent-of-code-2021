# part 1
with open("input-day08.txt") as input:
    total_digit_appearances = 0
    for line in input:
        output = line.split(" | ")[1].replace("\n", "")
        digits = output.split(" ")
        total_digit_appearances += len([d for d in digits if len(d) in [2, 4, 3, 7]])

    print(total_digit_appearances)


# part 2
with open("input-day08.txt") as f:
    total = 0
    for line in f:
        [input, output] = line.split(" | ")
        mapping = {}
        input_digits = input.split(" ")
        
        mapping['1'] = next(d for d in input_digits if len(d) == 2)
        mapping['4'] = next(d for d in input_digits if len(d) == 4)
        mapping['7'] = next(d for d in input_digits if len(d) == 3)
        mapping['8'] = next(d for d in input_digits if len(d) == 7)
        mapping['3'] = next(d for d in input_digits if len(d) == 5 and all(i in d for i in mapping['1']))
        mapping['9'] = next(d for d in input_digits if len(d) == 6 and all(i in d for i in mapping['1']) and all(i in d for i in mapping['4']))
        mapping['0'] = next(d for d in input_digits if len(d) == 6 and all(i in d for i in mapping['1']) and not all(i in d for i in mapping['4']))
        mapping['6'] = next(d for d in input_digits if len(d) == 6 and not all(i in d for i in mapping['1']))
        mapping['5'] = next(d for d in input_digits if len(d) == 5 and all(i in mapping['6'] for i in d))
        mapping['2'] = next(d for d in input_digits if len(d) == 5 and not all(i in mapping['9'] for i in d))

        output = output.replace("\n", "")
        digits = output.split(" ")

        inv_mapping = {"".join(sorted(v)): k for k, v in mapping.items()}
        total += int("".join([inv_mapping["".join(sorted(d))] for d in digits]))
    print(total)