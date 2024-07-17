input = "check_input"

# Open the input file and read it line by line.
with open(input, "r") as f:
    lines = f.read().splitlines()

# Get seeds from the list.
seed_list_with_title = lines[0].split()

# Strip out the title.
seed_list = seed_list_with_title[1:]
print(seed_list)

# Seed to soil maps:
seed_to_soil_maps = lines[]