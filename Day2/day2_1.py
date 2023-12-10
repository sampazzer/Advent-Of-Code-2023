"""
Information:
12 red
13 green
14 blue
"""
"""
fmtdList index:
index 0 = which game (the enumeration)
index 1 = string with the bog standard info. Not including "Game x:"
index 2 = list with per grab (grab 1 is index 0 within this list)
index 3 = list of numbers and colours independent of which grab it was
"""
# final list = list for getting the numbers of games that didnt have over the amount.
# fmtdList is the main list keeping track of the split up data
finalList = []
fmtdList = []

# the input file string
input = "input2_1"

# open the input file and read it line by line
with open(input, "r") as f:
    lines = f.read().splitlines()

# enumerated the input list to index the game numbers. Made it start from 1 rather than 0
enlist = list(enumerate(lines, 1))

# i is the enumeration, s is the string
for i, s in enlist:
    # allnumberscolours is a list of a list with the number and colour with the
    # white space stripped
    allnumberscolours = []
    # find the colon from the input so that I can get rid of everything up to and
    # including it as I dont need the game id's due to enumerating them
    # previously.
    findColon = s.find(":")
    # shortening the string
    strippedString = s[findColon + 2 :]
    # splitting the stripped down string on ; which gives each bag grab values
    perGrab = strippedString.split(";")
    # add into fmtdList the enumeration, string without the "game x:", perGrab
    # list due to using the split method
    fmtdList.append([i, strippedString, perGrab])
    for clrs in perGrab:
        # further splitting the each grab to overall game grabs
        clrsPerGrab = clrs.split(",")
        for clrs2 in clrsPerGrab:
            # stripping the white space around the list entries
            stripws = clrs2.strip()
            # split up this list
            splitnumberswords = stripws.split()
            # add the split numbers and colours list to allnumberscolours
            allnumberscolours.append(splitnumberswords)
    # add the allnumberscolours to the main list
    fmtdList[i - 1].append(allnumberscolours)

# finding out if any of the grabs for each game is above the allowed amount. If
# it is, dont add it to the final list. If it isnt add it to the final list.
for amount in range(len(fmtdList)):
    removefromlist = False
    for items, things in fmtdList[amount][3]:
        if things == "blue" and int(items) > 14:
            removefromlist = True
        elif things == "red" and int(items) > 12:
            removefromlist = True
        elif things == "green" and int(items) > 13:
            removefromlist = True
    if not removefromlist:
        finalList.append(amount + 1)

# print the final list and add the values together
print(finalList)
print(f"answer is {sum(finalList)}")
