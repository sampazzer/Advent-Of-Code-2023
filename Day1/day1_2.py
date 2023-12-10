from operator import itemgetter

from_word_position = 0
from_digit_position = 0

final_digit_list = []
text_data = "input1_1.txt"

# 0 = position, #1 = digit
digit_and_position_list = []


string_number_list = [
    ["one", "1"],
    ["two", "2"],
    ["three", "3"],
    ["four", "4"],
    ["five", "5"],
    ["six", "6"],
    ["seven", "7"],
    ["eight", "8"],
    ["nine", "9"],
]

with open(text_data, "r") as f:
    lines = f.read().splitlines()

for line in lines:
    for word, digit in string_number_list:
        while (word_index := line.find(word, from_word_position)) != -1:
            digit_and_position_list.append([word_index, digit])
            from_word_position = word_index + len(word)

        while (digit_index := line.find(digit, from_digit_position)) != -1:
            digit_and_position_list.append([digit_index, digit])
            from_digit_position = digit_index + 1

        from_word_position = 0
        from_digit_position = 0

    sorted_digit_and_position_list = sorted(digit_and_position_list, key=itemgetter(0))

    digit_and_position_list.clear()

    get_first_digit = sorted_digit_and_position_list[0][1]
    get_second_digit = sorted_digit_and_position_list[
        len(sorted_digit_and_position_list) - 1
    ][1]

    sorted_digit_and_position_list.clear()

    both_digits_together = get_first_digit + get_second_digit
    final_digit_list.append(int(both_digits_together))


# print(final_digit_list)
print(final_digit_list)
print(len(final_digit_list))
final_number = sum(final_digit_list)
print(final_number)
