import argparse
import util

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file")
args = parser.parse_args()

lines = util.parse_file(args.file)

matches = []
search_regex = r"mul\(([0-9]{1,3},[0-9]{1,3})\)"
for line in lines:
    matches += util.search_line(search_regex, line)

total = 0

for match in matches:
    first, second = match.split(',', 2)
    total += int(first) * int(second)

print(total)
