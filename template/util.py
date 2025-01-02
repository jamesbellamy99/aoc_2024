def parse_file(filename: str):
    with open(filename, "r") as file:
        lines = file.read().splitlines()
        return lines
