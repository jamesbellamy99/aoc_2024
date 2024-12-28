import argparse
import util

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file")
args = parser.parse_args()

reports = util.parse_file(args.file)

safe_reports = 0

for report in reports:
    if util.is_report_safe(report):
        safe_reports += 1

print(safe_reports)