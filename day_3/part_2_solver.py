import argparse
import util

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file")
args = parser.parse_args()

lines = util.parse_file(args.file)

matches = []
search_regex = r"(do\(\)|don't\(\))|mul\(([0-9]{1,3},[0-9]{1,3})\)"
for line in lines:
    matches += util.search_line(search_regex, line)

include = True
total = 0

for i in matches:
    match i:
        case "do()":
            include = True
        case "don't()":
            include = False
        case _:
            if include:
                first, second = i.split(',', 2)
                total += int(first) * int(second)

print(total)