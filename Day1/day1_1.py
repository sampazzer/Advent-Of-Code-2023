# Variables
text_data = "input1_1.txt"
digit_list = []
index_list = []
overall_list = []
my_index = 0

# need to input and parse the data.
# open the text file and put each line into a list
with open(text_data, "r") as f:
    lines = f.read().splitlines()

# read each line
for line in lines:
    print(line)
    # Get each character in that line
    for c in line:
        # If it is a digit then add it to my digit list
        # Also add the current index to my index list and
        # increment the index variable by 1.
        if c.isdigit():
            digit_list.append(c)
            index_list.append(my_index)
            my_index += 1

    print(index_list, digit_list)

    # Get the first descovered digit which will always be at
    # index_list[0].
    # Get the last descovered digit by sorting the index_list
    # in reverse order which will put the highest index at [0].
    lowest_digit = index_list[0]
    index_list.sort(reverse=True)
    highest_digit = index_list[0]

    # Concatonate the digits, turn them into an int and put them
    # in the over_list
    overall_list.append(int(digit_list[lowest_digit] + digit_list[highest_digit]))

    # Clear the lists that need it an the index ready for the next
    # line
    digit_list.clear()
    index_list.clear()
    my_index = 0

print(overall_list)

# Add the numbers together in the overall_list to get the final
# answer
final_answer = sum(overall_list)
print(final_answer)
