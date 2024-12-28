import util
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

list_1, list_2 = util.parse_file(args.file)

list_2_map = {}
for entry in list_2:
    if entry in list_2_map:
        list_2_map[entry] += 1
    else:
        list_2_map[entry] = 1

similarity_scores = [entry * list_2_map.get(entry, 0) for entry in list_1]
print(sum(similarity_scores))