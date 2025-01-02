import argparse
import util

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file")
args = parser.parse_args()

grid = util.parse_file(args.file)

xmas_found = 0

for x in range(0, grid.max_x + 1):
    for y in range(0, grid.max_y + 1):
        if grid.get_letter(x, y) == "X":
            for direction in util.Direction:
                try:
                    result = grid.get_letters_in_direction(x, y, direction, 3)
                    # We can ignore the X as we know we started with one
                    if result == "MAS":
                        xmas_found += 1
                except util.InvalidCoordinate:
                    pass

print(xmas_found)
