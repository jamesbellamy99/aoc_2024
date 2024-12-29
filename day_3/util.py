import re

def parse_file(filename: str):
    with open(filename, "r") as file:
        lines = file.readlines()
        return lines
    
def search_line(search_regex, line):
    matches = []
    maybe_tuples = re.findall(search_regex, line)
    for value in maybe_tuples:
        if isinstance(value, tuple):
            for subvalue in value:
                if subvalue != '':
                    matches.append(subvalue)
        else:
            matches.append(value)
    return matches