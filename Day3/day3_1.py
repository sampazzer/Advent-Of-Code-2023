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

# List of special characters
special_character_from_input = ["*", "%", "-", "#", "=", "@", "$", "/", "+", "&"]

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
                print("special char right of number")
                special_char_number_list.append(n[3])
                continue
            # If it isnt to the right then
            # Look below and one to the right
            for c in using_line[n[1] : n[2] + 2]:
                if c in special_character_from_input:
                    print("this is now working OK")
                    special_char_number_list.append(n[3])
                    break
        # If ending number index is last position then do the following
        if n[2] == len(lines[n[0]]) - 1:
            # Look to the left of the number
            if (lines[n[0]][n[1] - 1]) in special_character_from_input:
                print("special char left of number")
                special_char_number_list.append(n[3])
                continue
            # If it isnt to the left then
            # Look below and one to the left
            print(using_line[n[1] - 1 : n[2] + 1])
            for c in using_line[n[1] - 1 : n[2] + 1]:
                if c in special_character_from_input:
                    print("special char below on number far right")
                    special_char_number_list.append(n[3])
                    break
            continue
        # If number is not starting/ending in first/last positions
        if n[1] is not 0 and n[2] is not len(lines[n[0]]) - 1:
            same_line_chars = lines[n[0]][n[1] - 1] + lines[n[0]][n[2] + 1]
            lower_line_chars = lines[n[0] + 1][n[1] - 1 : n[2] + 2]
            all_lines_together = same_line_chars + lower_line_chars
            for c in all_lines_together:
                if c in special_character_from_input:
                    print("top line in the middle")
                    special_char_number_list.append(n[3])
                    break
            continue

    # ***NUMBERS BETWEEN FIRST AND LAST LINE***
    if 0 < n[0] < len(lines) - 1:
        print("not on first or last line")
        # ***This is such a better way of doing the search than what I did above.
        # ***It looks so much cleaner.
        # If number starting on first position search up to right, right, down to right
        if n[1] == 0:
            uppper_line_chars = lines[n[0] - 1][n[1] : n[2] + 2]
            same_line_chars = lines[n[0]][n[2] + 1]
            lower_line_chars = lines[n[0] + 1][n[1] : n[2] + 2]
            all_lines_together = uppper_line_chars + same_line_chars + lower_line_chars
            print(all_lines_together)
            for c in all_lines_together:
                if c in special_character_from_input:
                    print("special char on middle rows first index")
                    special_char_number_list.append(n[3])
                    break
        # If number ending on last position search up to left, left, down to left
        if n[2] == len(lines[n[0]]) - 1:
            print("middle number ending last index")
            uppper_line_chars = lines[n[0] - 1][n[1] - 1 : n[2] + 1]
            same_line_chars = lines[n[0]][n[1] - 1]
            lower_line_chars = lines[n[0] + 1][n[1] - 1 : n[2] + 1]
            all_lines_together = uppper_line_chars + same_line_chars + lower_line_chars
            print(all_lines_together)
            for c in all_lines_together:
                if c in special_character_from_input:
                    print("special char on middle rows last index")
                    special_char_number_list.append(n[3])
                    break
        # If number is not starting/ending in first/last positions
        if n[1] is not 0 and n[2] is not len(lines[n[0]]) - 1:
            print("I am in the middle of the middle")
            uppper_line_chars = lines[n[0] - 1][n[1] - 1 : n[2] + 2]
            same_line_chars = lines[n[0]][n[1] - 1] + lines[n[0]][n[2] + 1]
            lower_line_chars = lines[n[0] + 1][n[1] - 1 : n[2] + 2]
            all_lines_together = uppper_line_chars + same_line_chars + lower_line_chars
            print(all_lines_together)
            for c in all_lines_together:
                if c in special_character_from_input:
                    print("special char on middle rows first index")
                    special_char_number_list.append(n[3])
                    break

    # ***NUMBERS ON THE LAST LINE***
    if n[0] == len(lines) - 1:
        print("numbers on last line")
        # If number starts at position 0 search up right and right
        if n[1] == 0:
            uppper_line_chars = lines[n[0] - 1][n[1] : n[2] + 2]
            same_line_chars = lines[n[0]][n[2] + 1]
            all_lines_together = uppper_line_chars + same_line_chars
            print(all_lines_together)
            for c in all_lines_together:
                if c in special_character_from_input:
                    print("special char on last rows first index")
                    special_char_number_list.append(n[3])
                    break
        # If number ending on last position search up to left and left
        if n[2] == len(lines[n[0]]) - 1:
            uppper_line_chars = lines[n[0] - 1][n[1] - 1 : n[2] + 1]
            same_line_chars = lines[n[0]][n[1] - 1]
            all_lines_together = uppper_line_chars + same_line_chars
            print(all_lines_together)
            for c in all_lines_together:
                if c in special_character_from_input:
                    print("special char on last rows last index")
                    special_char_number_list.append(n[3])
                    break
        # If number is not starting/ending in first/last positions
        if n[1] is not 0 and n[2] is not len(lines[n[0]]) - 1:
            print("I am in the middle of the middle")
            uppper_line_chars = lines[n[0] - 1][n[1] - 1 : n[2] + 2]
            same_line_chars = lines[n[0]][n[1] - 1] + lines[n[0]][n[2] + 1]
            all_lines_together = uppper_line_chars + same_line_chars
            print(all_lines_together)
            for c in all_lines_together:
                if c in special_character_from_input:
                    print("special char on middle rows first index")
                    special_char_number_list.append(n[3])
                    break
for l in lines:
    print(l)
print(special_char_number_list)
int_special_char_number_list = [int(i) for i in special_char_number_list]
print(int_special_char_number_list)
print(sum(int_special_char_number_list))

# Result was: 514969
