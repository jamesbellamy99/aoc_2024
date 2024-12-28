import util
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file")
args = parser.parse_args()

list_1, list_2 = util.parse_file(args.file)

sorted_pairs = zip(list_1, list_2)
total = 0
for location_1, location_2 in sorted_pairs:
    difference = abs(location_1 - location_2)
    total += difference

print(total)
