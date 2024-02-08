# global variables
seeds = []
input = "check_input"


# open the input file and read it line by line.
with open(input, "r") as f:
    lines = f.read().splitlines()

print(lines[0])

# get seeds on line 1 and add them to the seeds list.
# this ignores the seeds: at the start of the string.
seeds = lines[0][6:].split()
print(seeds)
