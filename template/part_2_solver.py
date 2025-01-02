import argparse
import util

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file")
args = parser.parse_args()

lines = util.parse_file(args.file)
