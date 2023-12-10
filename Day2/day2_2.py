"""
Information:
12 red
13 grenn
14 blue
"""
"""
index 0 = which game
index 1 = string with all the grabs
index 3 = list with per grab (grab 1 is index 0 within this list)
"""
finalList = []
fmtdList = []
strippedclrs = []


input = "input2_1"

with open(input, "r") as f:
    lines = f.read().splitlines()

enlist = list(enumerate(lines, 1))

for i, s in enlist:
    allnumberscolours = []
    # print(i)
    # print(s)
    findColon = s.find(":")
    strippedString = s[findColon + 2 :]
    perGrab = strippedString.split(";")
    fmtdList.append([i, strippedString, perGrab])
    for clrs in perGrab:
        clrsPerGrab = clrs.split(",")
        # print("colours per grab: ", clrsPerGrab)
        for clrs2 in clrsPerGrab:
            stripws = clrs2.strip()
            # print(stripws)
            splitnumberswords = stripws.split()
            # print(splitnumberswords)
            allnumberscolours.append(splitnumberswords)
    fmtdList[i - 1].append(allnumberscolours)

# testlist = [["2", "blue"], ["5", "red"]]
# fmtdList[0].append(testlist)
# print(fmtdList[0][0])
# print(fmtdList[0][1])
# print(fmtdList[0][2])
# print(fmtdList)

# print(len(fmtdList[1][3]))
# print(len(fmtdList))

for amount in range(len(fmtdList)):
    removefromlist = False
    for items, things in fmtdList[amount][3]:
        if things == "blue" and int(items) > 14:
            # print("blue too big")
            removefromlist = True
        elif things == "red" and int(items) > 12:
            removefromlist = True
            # print("red too big")
        elif things == "green" and int(items) > 13:
            removefromlist = True
            # print("green too big")
    if not removefromlist:
        finalList.append(amount + 1)

print(finalList)
print(f"answer is {sum(finalList)}")
