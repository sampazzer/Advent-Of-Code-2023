input = "input4_1"

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

    # SECOND SET OF NUMBERS
    # Finding start position for the second set of numbers.
    position_of_separator_and_space_2 = i.find("|") + 2
    # Strip the string to have the second numbers.
    stripped_i_second_nums = i[position_of_separator_and_space_2:]
    # Split the string on space to get the separate numbers.
    list_second_nums = stripped_i_second_nums.split()

    # Comparing numbers in first list to second list. Adding them to an overall list if there are any matches.
    match_count = 0
    for nums in list_first_nums:
        if nums in list_second_nums:
            match_count += 1

    list_with_number_sets.append(match_count)

print(list_with_number_sets)

# For each of the numbers in the matches list
for index, numbers in enumerate(list_with_number_sets):
    # Repeat another loop the the amount of time we get from the match numbers
    for numbers2 in range(numbers):
        # Get the number from the current index of card duplicates
        number_buffer = card_duplicates[index]
        # Add that number to the next numbers in the array
        card_duplicates[index + numbers2 + 1] += number_buffer

print(sum(card_duplicates))

# Result was: 10425665
