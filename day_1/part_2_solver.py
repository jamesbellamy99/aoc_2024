list_1 = []
list_2 = []

with open("input.txt", "r") as file:
    input_pairs = file.readlines()
    for input_pair in input_pairs:
        entry_1, entry_2 = input_pair.split(maxsplit=2)
        list_1.append(int(entry_1))
        list_2.append(int(entry_2))

list_2_map = {}
for entry in list_2:
    if entry in list_2_map:
        list_2_map[entry] += 1
    else:
        list_2_map[entry] = 1

similarity_scores = [entry * list_2_map.get(entry, 0) for entry in list_1]
print(sum(similarity_scores))