input = "input4_1"

list_with_number_sets = []
final_number_list = []

# open the input file and read it line by line.
with open(input, "r") as f:
    lines = f.read().splitlines()

print(lines)

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
    if match_count > 0:
        list_with_number_sets.append(match_count)

# Looping through the matches and performing the maths using bitwise operators (putting a 1 and shifting it how ever many times theres a match -1)
for nums in list_with_number_sets:
    result = 1 << nums - 1
    final_number_list.append(result)

print(sum(final_number_list))

# Correct result: 21558
