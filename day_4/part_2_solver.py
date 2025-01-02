import argparse
import util

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file")
args = parser.parse_args()

grid = util.parse_file(args.file)

xmas_found = 0

for x in range(0, grid.max_x + 1):
    for y in range(0, grid.max_y + 1):
        if grid.get_letter(x, y) == "A":
            try:

                up_left_letter = grid.get_letters_in_direction(
                    x, y, util.Direction.UP_LEFT, 1
                )
                down_right_letter = grid.get_letters_in_direction(
                    x, y, util.Direction.DOWN_RIGHT, 1
                )
                up_right_letter = grid.get_letters_in_direction(
                    x, y, util.Direction.UP_RIGHT, 1
                )
                down_left_letter = grid.get_letters_in_direction(
                    x, y, util.Direction.DOWN_LEFT, 1
                )

                # Check that each diagonal contains a single M and a single S
                first_diag_letters = [up_left_letter, down_right_letter]
                second_diag_letters = [up_right_letter, down_left_letter]
                target_set = ["M", "S"]
                first_diag_letters.sort()
                second_diag_letters.sort()

                if first_diag_letters == second_diag_letters == target_set:
                    xmas_found += 1

            except util.InvalidCoordinate:
                pass

print(xmas_found)
