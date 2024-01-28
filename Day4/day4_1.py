input = "check_input"

# open the input file and read it line by line
with open(input, "r") as f:
    lines = f.read().splitlines()

print(lines)
