input = "check_input"

# open the input file and read it line by line.
with open(input, "r") as f:
    lines = f.read().splitlines()

print(lines[1])
# if lines[1] == "":
#     print("none")

newlist = [x for x in lines if x != ""]

print(newlist)
