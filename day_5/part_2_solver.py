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
invalid_updates = []

for update in updates:
    if util.is_update_valid(update, rule_map):
        valid_updates.append(update)
    else:
        invalid_updates.append(update)

print(f"Valid Updates: {valid_updates}")

print(f"Invalid Updates: {invalid_updates}")

fixed_updates = []
for invalid_update in invalid_updates:
    fixed_updates.append(util.fix_update(invalid_update, rule_map))

print(f"Fixed updates: {fixed_updates}")
    
total = 0
for fixed_update in fixed_updates:
    total += int(util.middle_page_of_update(fixed_update))

print(total)
