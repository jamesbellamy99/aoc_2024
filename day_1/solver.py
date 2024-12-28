list_1 = []
list_2 = []

with open("input.txt", "r") as file:
    input_pairs = file.readlines()
    for input_pair in input_pairs:
        entry_1, entry_2 = input_pair.split(maxsplit=2)
        list_1.append(int(entry_1))
        list_2.append(int(entry_2))

list_1.sort()
list_2.sort()

sorted_pairs = zip(list_1, list_2)
total = 0
for location_1, location_2 in sorted_pairs:
    difference = abs(location_1 - location_2)
    total += difference

print(total)
