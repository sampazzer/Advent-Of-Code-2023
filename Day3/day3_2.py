import time
import math

# the input file string
input = "input3_1"

""" I wrote this to find the special characters in the input so I didnt have
to use all special characters and check for ones I didnt need to.
It reads the lines and adds the characters to a list if they arent already
in it
for line in lines:
    for c in line:
        if not c.isdigit() and not c == ".":
            if not c in special_character_from_input:
                special_character_from_input.append(c)

print(special_character_from_input)
"""

# Index for saving special char dictionary
# Dict template: {"index": 123, "number": 123}
temp_dict_list = []
dict_index_list = []

# List of special characters
special_character_from_input = ["*"]

# List of numbers which are next to special chacracters
special_char_number_list = []


# List of special characters
# I want to check for numbers in the line and grab an index. NUMBER POSITION INDEX (non perm)
# I want to check how many digits the number is. NUMBER LENGTH INDEX (non perm)
# I want to save the number. ACTUAL NUMBER VALUE (perm)
# ------- LINE 0
# -42-13- LINE 1
# ------- LINE 2

# all_numbers_list:
# line index / starting number index / end digit index / number
# list = [[0,0,2,413],[1,2,3,67]]

all_numbers_list = []

# open the input file and read it line by line
with open(input, "r") as f:
    lines = f.read().splitlines()

# enumerated the input list to index the game numbers. Made it start from 1 rather than 0
enlist = list(enumerate(lines, 0))

# linei is the enumeration, l is the line
for linei, l in enlist:
    digit_start = False
    print(l)
    # chari is the enumeration, c is the character in the line
    for chari, c in enumerate(l, 0):
        # do this for the first digit recognised
        if c.isdigit() and digit_start:
            # If its a digit and the first one has alread been sorted then concat next digit
            number += str(c)
        elif c.isdigit() and not digit_start:
            # print(linei, chari, c)
            # If its the first digit then save the index of it and save the first number
            # and save the line index
            start_digit_index = chari
            number = str(c)
            line_number_index = linei
            digit_start = True
        if (not c.isdigit() or chari == len(l) - 1) and digit_start:
            # If its not a digit but we have started recording the digits then set digit_start
            # to false and add all the information to the main list
            # If its not a digit then the index should be -1 as the number was in the previous index
            if not c.isdigit():
                end_digit_index = chari - 1
            # If were in this function then its because were at the end of the line therefore the
            # number index should be the last position
            else:
                end_digit_index = chari
            digit_start = False
            all_numbers_list.append(
                [line_number_index, start_digit_index, end_digit_index, number]
            )


print(all_numbers_list)
print(len(lines))

# Need to loop again and see if any special characters are next to any of the numbers
# in "all_numbers_list"

# 93--321 LINE 0
# -42-13- LINE 1
# ------- LINE 2
# all_numbers_list:
# line index / starting number index / end digit index / number
# list = [[0,0,2,413],[1,2,3,67]]
for n in all_numbers_list:
    print("n in all numbers list: ", n)
    # ***NUMBERS ON FIRST LINE***
    # If on line 0 then have some other stuff checked
    if n[0] == 0:
        # Use the line below our current line to search for special char
        using_line = lines[n[0] + 1]
        # If starting number index is 0 then do the following
        if n[1] == 0:
            # Look to the right of the number
            if lines[n[0]][n[2] + 1] in special_character_from_input:
                append_number_to_index = False
                # Check for index already in list
                for items in dict_index_list:
                    # If we find the index already in the list then add the number to that index
                    if items["index"] == str(n[0]) + "/" + str(n[2] + 1):
                        items["number"].append(n[3])
                        append_number_to_index = True
                # If we dont find the index already in the list then add the index with the number
                if not append_number_to_index:
                    my_index = str(n[0]) + "/" + str(n[2] + 1)
                    dict_index_list.append({"index": my_index, "number": [n[3]]})
            # If it isnt to the right then
            # Look below and one to the right
            for i, c in enumerate(using_line[n[1] : n[2] + 2], n[1]):
                append_number_to_index = False
                if c in special_character_from_input:
                    for items in dict_index_list:
                        # If we find the index already in the list then add the number to that index
                        if items["index"] == str(n[0] + 1) + "/" + str(i):
                            items["number"].append(n[3])
                            append_number_to_index = True
                    # If we dont find the index already in the list then add the index with the number
                    if not append_number_to_index:
                        my_index = str(n[0] + 1) + "/" + str(i)
                        dict_index_list.append({"index": my_index, "number": [n[3]]})
        # If ending number index is last position then do the following
        if n[2] == len(lines[n[0]]) - 1:
            # Look to the left of the number
            if (lines[n[0]][n[1] - 1]) in special_character_from_input:
                append_number_to_index = False
                # Check for index already in list
                for items in dict_index_list:
                    # If we find the index already in the list then add the number to that index
                    if items["index"] == str(n[0]) + "/" + str(n[1] - 1):
                        items["number"].append(n[3])
                        append_number_to_index = True
                # If we dont find the index already in the list then add the index with the number
                if not append_number_to_index:
                    my_index = str(n[0]) + "/" + str(n[1] - 1)
                    dict_index_list.append({"index": my_index, "number": [n[3]]})
            # If it isnt to the left then
            # Look below and one to the left
            print(using_line[n[1] - 1 : n[2] + 1])
            for i, c in enumerate(using_line[n[1] - 1 : n[2] + 1], n[1] - 1):
                append_number_to_index = False
                if c in special_character_from_input:
                    for items in dict_index_list:
                        # If we find the index already in the list then add the number to that index
                        if items["index"] == str(n[0] + 1) + "/" + str(i):
                            items["number"].append(n[3])
                            append_number_to_index = True
                    # If we dont find the index already in the list then add the index with the number
                    if not append_number_to_index:
                        my_index = str(n[0] + 1) + "/" + str(i)
                        dict_index_list.append({"index": my_index, "number": [n[3]]})
        # If number is not starting/ending in first/last positions
        if n[1] is not 0 and n[2] is not len(lines[n[0]]) - 1:
            # Check the same line characters
            same_line_chars = lines[n[0]][n[1] - 1] + lines[n[0]][n[2] + 1]
            for i, c in enumerate(same_line_chars):
                # If its a special character and its the first iteration then it has to be to the left
                if c in special_character_from_input and i == 0:
                    append_number_to_index = False
                    # Check for index already in list
                    for items in dict_index_list:
                        # If we find the index already in the list then add the number to that index
                        if items["index"] == str(n[0]) + "/" + str(n[1] - 1):
                            items["number"].append(n[3])
                            append_number_to_index = True
                    # If we dont find the index already in the list then add the index with the number
                    if not append_number_to_index:
                        my_index = str(n[0]) + "/" + str(n[1] - 1)
                        dict_index_list.append({"index": my_index, "number": [n[3]]})
                # If its a special character and its the second iteration then it has to be to the left
                if c in special_character_from_input and i == 1:
                    append_number_to_index = False
                    # Check for index already in list
                    for items in dict_index_list:
                        # If we find the index already in the list then add the number to that index
                        if items["index"] == str(n[0]) + "/" + str(n[2] + 1):
                            items["number"].append(n[3])
                            append_number_to_index = True
                    # If we dont find the index already in the list then add the index with the number
                    if not append_number_to_index:
                        my_index = str(n[0]) + "/" + str(n[2] + 1)
                        dict_index_list.append({"index": my_index, "number": [n[3]]})

            # Check lower line characters
            lower_line_chars = lines[n[0] + 1][n[1] - 1 : n[2] + 2]
            for i, c in enumerate(lower_line_chars, n[1] - 1):
                append_number_to_index = False
                if c in special_character_from_input:
                    for items in dict_index_list:
                        # If we find the index already in the list then add the number to that index
                        if items["index"] == str(n[0] + 1) + "/" + str(i):
                            items["number"].append(n[3])
                            append_number_to_index = True
                    # If we dont find the index already in the list then add the index with the number
                    if not append_number_to_index:
                        my_index = str(n[0] + 1) + "/" + str(i)
                        dict_index_list.append({"index": my_index, "number": [n[3]]})

    # ***NUMBERS BETWEEN FIRST AND LAST LINE***
    if 0 < n[0] < len(lines) - 1:
        print("not on first or last line")
        # ***This is such a better way of doing the search than what I did above.
        # ***It looks so much cleaner.
        # If number starting on first position search up to right, right, down to right
        if n[1] == 0:
            upper_line_chars = lines[n[0] - 1][n[1] : n[2] + 2]
            for i, c in enumerate(upper_line_chars, n[1]):
                append_number_to_index = False
                if c in special_character_from_input:
                    for items in dict_index_list:
                        # If we find the index already in the list then add the number to that index
                        if items["index"] == str(n[0] - 1) + "/" + str(i):
                            items["number"].append(n[3])
                            append_number_to_index = True
                    # If we dont find the index already in the list then add the index with the number
                    if not append_number_to_index:
                        my_index = str(n[0] - 1) + "/" + str(i)
                        dict_index_list.append({"index": my_index, "number": [n[3]]})

            same_line_chars = lines[n[0]][n[2] + 1]
            for i, c in enumerate(same_line_chars, n[2] + 1):
                append_number_to_index = False
                if c in special_character_from_input:
                    for items in dict_index_list:
                        # If we find the index already in the list then add the number to that index
                        if items["index"] == str(n[0]) + "/" + str(i):
                            items["number"].append(n[3])
                            append_number_to_index = True
                    # If we dont find the index already in the list then add the index with the number
                    if not append_number_to_index:
                        my_index = str(n[0]) + "/" + str(i)
                        dict_index_list.append({"index": my_index, "number": [n[3]]})

            lower_line_chars = lines[n[0] + 1][n[1] : n[2] + 2]
            for i, c in enumerate(lower_line_chars, n[1]):
                append_number_to_index = False
                if c in special_character_from_input:
                    for items in dict_index_list:
                        # If we find the index already in the list then add the number to that index
                        if items["index"] == str(n[0] + 1) + "/" + str(i):
                            items["number"].append(n[3])
                            append_number_to_index = True
                    # If we dont find the index already in the list then add the index with the number
                    if not append_number_to_index:
                        my_index = str(n[0] + 1) + "/" + str(i)
                        dict_index_list.append({"index": my_index, "number": [n[3]]})

        # If number ending on last position search up to left, left, down to left
        if n[2] == len(lines[n[0]]) - 1:
            print("middle number ending last index")
            upper_line_chars = lines[n[0] - 1][n[1] - 1 : n[2] + 1]
            for i, c in enumerate(upper_line_chars, n[1] - 1):
                append_number_to_index = False
                if c in special_character_from_input:
                    for items in dict_index_list:
                        # If we find the index already in the list then add the number to that index
                        if items["index"] == str(n[0] - 1) + "/" + str(i):
                            items["number"].append(n[3])
                            append_number_to_index = True
                    # If we dont find the index already in the list then add the index with the number
                    if not append_number_to_index:
                        my_index = str(n[0] - 1) + "/" + str(i)
                        dict_index_list.append({"index": my_index, "number": [n[3]]})

            same_line_chars = lines[n[0]][n[1] - 1]
            for i, c in enumerate(same_line_chars, n[1] - 1):
                append_number_to_index = False
                if c in special_character_from_input:
                    for items in dict_index_list:
                        # If we find the index already in the list then add the number to that index
                        if items["index"] == str(n[0]) + "/" + str(i):
                            items["number"].append(n[3])
                            append_number_to_index = True
                    # If we dont find the index already in the list then add the index with the number
                    if not append_number_to_index:
                        my_index = str(n[0]) + "/" + str(i)
                        dict_index_list.append({"index": my_index, "number": [n[3]]})

            lower_line_chars = lines[n[0] + 1][n[1] - 1 : n[2] + 1]
            for i, c in enumerate(lower_line_chars, n[1] - 1):
                append_number_to_index = False
                if c in special_character_from_input:
                    for items in dict_index_list:
                        # If we find the index already in the list then add the number to that index
                        if items["index"] == str(n[0] + 1) + "/" + str(i):
                            items["number"].append(n[3])
                            append_number_to_index = True
                    # If we dont find the index already in the list then add the index with the number
                    if not append_number_to_index:
                        my_index = str(n[0] + 1) + "/" + str(i)
                        dict_index_list.append({"index": my_index, "number": [n[3]]})

        # If number is not starting/ending in first/last positions
        # Upper characters
        if n[1] is not 0 and n[2] is not len(lines[n[0]]) - 1:
            upper_line_chars = lines[n[0] - 1][n[1] - 1 : n[2] + 2]
            for i, c in enumerate(upper_line_chars, n[1] - 1):
                append_number_to_index = False
                if c in special_character_from_input:
                    for items in dict_index_list:
                        # If we find the index already in the list then add the number to that index
                        if items["index"] == str(n[0] - 1) + "/" + str(i):
                            items["number"].append(n[3])
                            append_number_to_index = True
                    # If we dont find the index already in the list then add the index with the number
                    if not append_number_to_index:
                        my_index = str(n[0] - 1) + "/" + str(i)
                        dict_index_list.append({"index": my_index, "number": [n[3]]})

            # Same line characters
            same_line_chars = lines[n[0]][n[1] - 1] + lines[n[0]][n[2] + 1]
            for i, c in enumerate(same_line_chars):
                # If its a special character and its the first iteration then it has to be to the left
                if c in special_character_from_input and i == 0:
                    append_number_to_index = False
                    # Check for index already in list
                    for items in dict_index_list:
                        # If we find the index already in the list then add the number to that index
                        if items["index"] == str(n[0]) + "/" + str(n[1] - 1):
                            items["number"].append(n[3])
                            append_number_to_index = True
                    # If we dont find the index already in the list then add the index with the number
                    if not append_number_to_index:
                        my_index = str(n[0]) + "/" + str(n[1] - 1)
                        dict_index_list.append({"index": my_index, "number": [n[3]]})
                # If its a special character and its the second iteration then it has to be to the left
                if c in special_character_from_input and i == 1:
                    append_number_to_index = False
                    # Check for index already in list
                    for items in dict_index_list:
                        # If we find the index already in the list then add the number to that index
                        if items["index"] == str(n[0]) + "/" + str(n[2] + 1):
                            items["number"].append(n[3])
                            append_number_to_index = True
                    # If we dont find the index already in the list then add the index with the number
                    if not append_number_to_index:
                        my_index = str(n[0]) + "/" + str(n[2] + 1)
                        dict_index_list.append({"index": my_index, "number": [n[3]]})

            # Lower characters
            lower_line_chars = lines[n[0] + 1][n[1] - 1 : n[2] + 2]
            for i, c in enumerate(lower_line_chars, n[1] - 1):
                append_number_to_index = False
                if c in special_character_from_input:
                    for items in dict_index_list:
                        # If we find the index already in the list then add the number to that index
                        if items["index"] == str(n[0] + 1) + "/" + str(i):
                            items["number"].append(n[3])
                            append_number_to_index = True
                    # If we dont find the index already in the list then add the index with the number
                    if not append_number_to_index:
                        my_index = str(n[0] + 1) + "/" + str(i)
                        dict_index_list.append({"index": my_index, "number": [n[3]]})

    # ***NUMBERS ON THE LAST LINE***
    if n[0] == len(lines) - 1:
        print("numbers on last line")
        # If number starts at position 0 search up right and right
        if n[1] == 0:
            upper_line_chars = lines[n[0] - 1][n[1] : n[2] + 2]
            for i, c in enumerate(upper_line_chars, n[1]):
                append_number_to_index = False
                if c in special_character_from_input:
                    for items in dict_index_list:
                        # If we find the index already in the list then add the number to that index
                        if items["index"] == str(n[0] - 1) + "/" + str(i):
                            items["number"].append(n[3])
                            append_number_to_index = True
                    # If we dont find the index already in the list then add the index with the number
                    if not append_number_to_index:
                        my_index = str(n[0] - 1) + "/" + str(i)
                        dict_index_list.append({"index": my_index, "number": [n[3]]})
            same_line_chars = lines[n[0]][n[2] + 1]
            for i, c in enumerate(same_line_chars, n[2] + 1):
                append_number_to_index = False
                if c in special_character_from_input:
                    for items in dict_index_list:
                        # If we find the index already in the list then add the number to that index
                        if items["index"] == str(n[0]) + "/" + str(i):
                            items["number"].append(n[3])
                            append_number_to_index = True
                    # If we dont find the index already in the list then add the index with the number
                    if not append_number_to_index:
                        my_index = str(n[0]) + "/" + str(i)
                        dict_index_list.append({"index": my_index, "number": [n[3]]})

        # If number ending on last position search up to left and left
        if n[2] == len(lines[n[0]]) - 1:
            upper_line_chars = lines[n[0] - 1][n[1] - 1 : n[2] + 1]
            for i, c in enumerate(upper_line_chars, n[1] - 1):
                append_number_to_index = False
                if c in special_character_from_input:
                    for items in dict_index_list:
                        # If we find the index already in the list then add the number to that index
                        if items["index"] == str(n[0] - 1) + "/" + str(i):
                            items["number"].append(n[3])
                            append_number_to_index = True
                    # If we dont find the index already in the list then add the index with the number
                    if not append_number_to_index:
                        my_index = str(n[0] - 1) + "/" + str(i)
                        dict_index_list.append({"index": my_index, "number": [n[3]]})
            same_line_chars = lines[n[0]][n[1] - 1]
            for i, c in enumerate(same_line_chars, n[1] - 1):
                append_number_to_index = False
                if c in special_character_from_input:
                    for items in dict_index_list:
                        # If we find the index already in the list then add the number to that index
                        if items["index"] == str(n[0]) + "/" + str(i):
                            items["number"].append(n[3])
                            append_number_to_index = True
                    # If we dont find the index already in the list then add the index with the number
                    if not append_number_to_index:
                        my_index = str(n[0]) + "/" + str(i)
                        dict_index_list.append({"index": my_index, "number": [n[3]]})

        # If number is not starting/ending in first/last positions
        if n[1] is not 0 and n[2] is not len(lines[n[0]]) - 1:
            print("I am in the middle of the middle")
            upper_line_chars = lines[n[0] - 1][n[1] - 1 : n[2] + 2]
            for i, c in enumerate(upper_line_chars, n[1] - 1):
                append_number_to_index = False
                if c in special_character_from_input:
                    for items in dict_index_list:
                        # If we find the index already in the list then add the number to that index
                        if items["index"] == str(n[0] - 1) + "/" + str(i):
                            items["number"].append(n[3])
                            append_number_to_index = True
                    # If we dont find the index already in the list then add the index with the number
                    if not append_number_to_index:
                        my_index = str(n[0] - 1) + "/" + str(i)
                        dict_index_list.append({"index": my_index, "number": [n[3]]})
            same_line_chars = lines[n[0]][n[1] - 1] + lines[n[0]][n[2] + 1]
            for i, c in enumerate(same_line_chars):
                # If its a special character and its the first iteration then it has to be to the left
                if c in special_character_from_input and i == 0:
                    append_number_to_index = False
                    # Check for index already in list
                    for items in dict_index_list:
                        # If we find the index already in the list then add the number to that index
                        if items["index"] == str(n[0]) + "/" + str(n[1] - 1):
                            items["number"].append(n[3])
                            append_number_to_index = True
                    # If we dont find the index already in the list then add the index with the number
                    if not append_number_to_index:
                        my_index = str(n[0]) + "/" + str(n[1] - 1)
                        dict_index_list.append({"index": my_index, "number": [n[3]]})
                # If its a special character and its the second iteration then it has to be to the left
                if c in special_character_from_input and i == 1:
                    append_number_to_index = False
                    # Check for index already in list
                    for items in dict_index_list:
                        # If we find the index already in the list then add the number to that index
                        if items["index"] == str(n[0]) + "/" + str(n[2] + 1):
                            items["number"].append(n[3])
                            append_number_to_index = True
                    # If we dont find the index already in the list then add the index with the number
                    if not append_number_to_index:
                        my_index = str(n[0]) + "/" + str(n[2] + 1)
                        dict_index_list.append({"index": my_index, "number": [n[3]]})


for l in lines:
    print(l)

print("dict index list ", dict_index_list)

# Find entries with 2 or more numbers in them so we can times
# them together and add them
results_list = []
for items in dict_index_list:
    # print(items["number"])
    if len(items["number"]) >= 2:
        int_result = 0
        temp_list_result = []
        for numbers in items["number"]:
            temp_list_result.append(int(numbers))
        results_list.append(math.prod(temp_list_result))
result = sum(results_list)
print(result)

""" NOTES:
- Special character is now only *
- When searching for special char dont break the loop, has to check the whole way aorund.
- Need to index * somehow
- When we find a number add its index to a list of dict's along with the numbers tied to it
"""
