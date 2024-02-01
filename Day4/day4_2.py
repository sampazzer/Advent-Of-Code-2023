input = "check_input"

list_with_number_sets = []

# open the input file and read it line by line.
with open(input, "r") as f:
    lines = f.read().splitlines()

# Create list for keeping track of the card duplicates. Done using List Comprehension. Creates a list as long as the length of the input lines and fills it with zeros.
card_duplicates = [1 for x in range(len(lines))]

for i in lines:
    # FIRST SET OF NUMBERS
    # Finding start position to split the first numbers from.
    position_of_colon_and_space = i.find(":") + 2
    # Finding end position to split the first numbers from.
    position_of_separator_and_space = i.find("|") - 1
    # Strip the string to to have the first numbers.
    stripped_i_first_nums = i[
        position_of_colon_and_space:position_of_separator_and_space
    ]
    # Split the string on space to get the separate numbers.
    list_first_nums = stripped_i_first_nums.split()
    print(list_first_nums)

    # SECOND SET OF NUMBERS
    # Finding start position for the second set of numbers.
    position_of_separator_and_space_2 = i.find("|") + 2
    # Strip the string to have the second numbers.
    stripped_i_second_nums = i[position_of_separator_and_space_2:]
    # Split the string on space to get the separate numbers.
    list_second_nums = stripped_i_second_nums.split()
    print(list_second_nums)

    # Comparing numbers in first list to second list. Adding them to an overall list if there are any matches.
    match_count = 0
    for nums in list_first_nums:
        if nums in list_second_nums:
            match_count += 1

    list_with_number_sets.append(match_count)
    print(list_with_number_sets)

"""
list_with_number_sets:
     1  2  3  4  5  6
    [4, 2, 2, 1, 0, 0]
card_duplicates:
    [1, 1, 1, 1, 1, 1]
    [1, 2, 4, 4, 2, 1]

final result should be:
    [1, 2, 4, 8, 14, 1]
"""

print(list_with_number_sets)
# Need to find which card has got the matching numbers so that I can understand which extra ones are going to be created. can do this from an enumeration+1

# The for loop will take the current index i1 from list_with_number_sets A.
# Nested for loop to take index i1
# It adds one to the current index i2 in card_duplicates B.

# Gets amount of matching numbers
print(card_duplicates)

for index, numbers in enumerate(list_with_number_sets):
    for locations in range(numbers):
        card_duplicates[index + 1]
