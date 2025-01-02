def parse_file(filename: str):
    with open(filename, "r") as file:
        lines = file.read().splitlines()
        seperation = lines.index("")
        rules = lines[:seperation]
        updates = lines[seperation + 1 :]
        return rules, updates


def parse_rules(rules):
    rule_map = {}
    for rule in rules:
        before, after = rule.split("|")
        if before in rule_map:
            current = rule_map[before]
            rule_map[before] = current + [after]
        else:
            rule_map[before] = [after]
    return rule_map


def is_update_valid(update, rule_map):
    update_values = update.split(",")
    for index, value in enumerate(update_values):
        values_that_have_to_come_after = rule_map.get(value)
        if values_that_have_to_come_after:
            previous_values = update_values[:index]
            if len(set(previous_values) & set(values_that_have_to_come_after)):
                return False
    return True


def middle_page_of_update(update):
    update_values = update.split(",")
    return update_values[len(update_values) // 2]


def fix_update(update, rule_map):
    # I don't like this, but it works
    # it relies on there being at most
    # one value that doesn't have a rule
    # which is fine for this but doesn't make sense
    update_values = update.split(",")
    while True:
        switched_anything = False
        for i in range(0, len(update_values)):
            for j in range(i + 1, len(update_values)):
                values_that_have_to_come_after = rule_map.get(update_values[i], [])
                if not update_values[j] in values_that_have_to_come_after:
                    update_values[i], update_values[j] = (
                        update_values[j],
                        update_values[i],
                    )
                    switched_anything = True
        if not switched_anything:
            return ",".join(update_values)
