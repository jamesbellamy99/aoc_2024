def parse_file(filename: str):
    list_1 = []
    list_2 = []

    with open(filename, "r") as file:
        input_pairs = file.readlines()
        for input_pair in input_pairs:
            entry_1, entry_2 = input_pair.split(maxsplit=2)
            list_1.append(int(entry_1))
            list_2.append(int(entry_2))
    
    list_1.sort()
    list_2.sort()
    return list_1, list_2