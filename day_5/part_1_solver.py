import argparse
import util

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file")
args = parser.parse_args()

rules, updates = util.parse_file(args.file)
rule_map = util.parse_rules(rules)

print(f"Rules: {rules}")
print(f"Rule Map: {rule_map}")
print(f"Updates: {updates}")

valid_updates = []

for update in updates:
    if util.is_update_valid(update, rule_map):
        valid_updates.append(update)

print(f"Valid Updates: {valid_updates}")

total = 0
for valid_update in valid_updates:
    total += int(util.middle_page_of_update(valid_update))

print(total)
