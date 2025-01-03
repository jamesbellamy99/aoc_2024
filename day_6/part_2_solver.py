import argparse
import itertools
import multiprocessing

import tqdm
import util


def test_obstructions(args):
    coord, input = args
    map = util.Map(input)
    x, y = coord
    map.add_custom_obstruction(x, y)
    map.run()
    return map.result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file")
    args = parser.parse_args()

    input = util.parse_file(args.file)

    origional_map = util.Map(input)
    origional_map.run()

    visited_locations = origional_map.get_all_visited_locations()

    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    loops = 0
    results = tqdm.tqdm(
        pool.imap_unordered(
            test_obstructions, zip(visited_locations, itertools.repeat(input))
        ),
        total=len(visited_locations),
    )
    for result in results:
        if result == util.Result.Looping:
            loops += 1
    pool.close()
    print(f"Solutions with loops: {loops}")
