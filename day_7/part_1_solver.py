import argparse
import util

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file")
args = parser.parse_args()

entries = util.parse_file(args.file)
valid_opts = ["+", "*"]
valid_targets = set()
for target, input in entries:
    num_opts = util.number_of_operators(input)
    opt_combos = util.get_possible_operator_combos(valid_opts, num_opts)
    for opts in opt_combos:
        if util.apply_operators(int(target), input, opts):
            valid_targets.add(int(target))

print(sum(valid_targets))
