input = "check_input"

# Open the input file and read it line by line.
with open(input, "r") as f:
    lines = f.read().splitlines()

times = lines[0].split()[1:]
distances = lines[1].split()[1:]
