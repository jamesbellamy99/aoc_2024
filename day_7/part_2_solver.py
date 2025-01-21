import argparse
import util
import multiprocessing
import tqdm

valid_opts = ["+", "*", "||"]


def process_entry(entry):
    target, input = entry
    num_opts = util.number_of_operators(input)
    opt_combos = util.get_possible_operator_combos(valid_opts, num_opts)
    # This could be sped up by processing the opt combos in parallel
    # as well, but then early returns become more complex
    for opts in opt_combos:
        if util.apply_operators(int(target), input, opts):
            return int(target)
    return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file")
    args = parser.parse_args()

    entries = util.parse_file(args.file)
    total = 0
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    results = tqdm.tqdm(
        pool.imap_unordered(
            process_entry, entries
        ),
        total=len(entries),
    )
    for result in results:
        if result:
            total += result

    pool.close()
    print(total)
