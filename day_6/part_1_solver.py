import argparse

import util

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file")
args = parser.parse_args()

input = util.parse_file(args.file)
map = util.Map(input)
map.run()

print(f"Visited Locations: {map.count_visited()}")
