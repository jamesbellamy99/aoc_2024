import enum
import itertools


def parse_file(filename: str):
    with open(filename, "r") as file:
        lines = file.read().splitlines()
        data = []
        for line in lines:
            target, input = line.split(":")
            split_input = input.split()
            data.append((target, split_input))
        return data


def apply_operators(target, numbers, operators):
    total = int(numbers[0])
    index = 1
    for operator in operators:
        match operator:
            case "+":
                total += int(numbers[index])
            case "*":
                total = total * int(numbers[index])
            case "||":
                total = int(str(total) + numbers[index])
        index += 1
        # This optimisation only work because the problem doesn't support -
        if total > target:
            return False
    return total == target


def number_of_operators(numbers):
    return len(numbers) - 1


def get_possible_operator_combos(valid_opts, number_of_operators):
    opts = []
    for opt in itertools.product(valid_opts, repeat=number_of_operators):
        list_opt = list(opt)
        opts.append(list_opt)
    return opts
