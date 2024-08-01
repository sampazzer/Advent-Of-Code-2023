from operator import itemgetter

input = "input5_1"


# Function to make my almanac ranges
def ranges_make(range_list):
    ranges_list = []
    for range in range_list:
        nums = range.split()
        start_point = int(nums[1])
        end_point = start_point + (int(nums[2]) - 1)
        dest_diff = int(nums[0]) - int(nums[1])
        ranges_list.append([start_point, end_point, dest_diff])
    return ranges_list


# FUNCTION
# I need a function that takes in two lists. First is the sorted ranges. Second is the almanac ranges.
# Needs to return a list of ranges to be used in the next call of this function.
def ranges_sort(ranges, almanacs):
    new_ranges = []
    for range in ranges:
        full_range_mapped = False
        for almanac in almanacs:
            start_within_range = False
            end_within_range = False
            # Check if start is within range
            if range[0] >= almanac[0] and range[0] <= almanac[1]:
                start_within_range = True

            # Check if end is within range
            if range[1] >= almanac[0] and range[1] <= almanac[1]:
                end_within_range = True

            # If only the start is within range then:
            # [start_seed_range, end_soil_range] : translate this with the difference, append to new seed ranges
            # [end_soil_range + 1, end_seed_range] : this is untouched as it doesnt fall in range, adjust the new range to reflect what has been mapped
            if start_within_range and not end_within_range:
                new_ranges.append(
                    [
                        range[0] + almanac[2],
                        almanac[1] + almanac[2],
                    ]
                )
                range[0] = almanac[1] + 1

            # If only the end is within range then:
            # [start_soil_range, end_seed_range] : translate this with the difference, append to new seed ranges
            # [start_seed_range, start_soil_range - 1] : this is untouched as it doesnt fall in range, adjust the new range to reflect what has been mapped
            if not start_within_range and end_within_range:
                new_ranges.append(
                    [
                        almanac[0] + almanac[2],
                        range[1] + almanac[2],
                    ]
                )
                range[1] = almanac[0] - 1

            # If the start and end are within range then:
            # [start_seed_range, end_seed_range] : translate this with the difference, append to new seed ranges
            # this also means that all the numbers have been mapped from this range and we can break the loop
            if start_within_range and end_within_range:
                new_ranges.append(
                    [
                        range[0] + almanac[2],
                        range[1] + almanac[2],
                    ]
                )
                full_range_mapped = True
                break
        # Add the unmapped range to the list if it hasnt all been mapped
        if not full_range_mapped:
            new_ranges.append([range[0], range[1]])
    return new_ranges


# Open the input file and read it line by line.
with open(input, "r") as f:
    lines = f.read().splitlines()

# Get seeds from the list.
seed_list_with_title = lines[0].split()

# Strip out the title.
seed_list = seed_list_with_title[1:]

# Seed to soil maps:
seed_to_soil_maps = lines[3:50]

# Soil to fertilizer maps:
soil_to_fertilizer_maps = lines[52:70]

# Fertilizer to water maps:
fertilizer_to_water_maps = lines[72:84]

# Water to light maps:
water_to_light_maps = lines[86:135]

# Light to temperature maps:
light_to_temperature_maps = lines[137:167]

# Temperature to humidity maps:
temperature_to_humidity_maps = lines[169:192]

# Humidity to location maps:
humidity_to_location_maps = lines[194:237]

# Seed list ranges
seed_list_ranges = []
# Counter to keep track of if its 0 which equals the start number or 1 which equals the range of numbers
seed_loop_counter = 0
# Loop to get the new seed ranges
for seed in seed_list:
    # If the counter is 0 then its a start point
    if seed_loop_counter == 0:
        # Save the start point number
        seed_start_point = int(seed)
        # Increment the counter
        seed_loop_counter += 1
        # If the counter is 1 then its a range
    elif seed_loop_counter == 1:
        # Append the new list with all the numbers from the start point to the end of the range.
        seed_end_point = seed_start_point + int(seed)
        seed_loop_counter = 0
        seed_list_ranges.append([seed_start_point, seed_end_point])

# Get the almanac ranges
soil_list_ranges = ranges_make(seed_to_soil_maps)
fertilizer_list_ranges = ranges_make(soil_to_fertilizer_maps)
water_list_ranges = ranges_make(fertilizer_to_water_maps)
light_list_ranges = ranges_make(water_to_light_maps)
temperature_list_ranges = ranges_make(light_to_temperature_maps)
humidity_list_ranges = ranges_make(temperature_to_humidity_maps)
location_list_ranges = ranges_make(humidity_to_location_maps)

# Feed the ranges into the ranges_sort function to get the resultant mapped ranges.
new_soil_ranges = ranges_sort(seed_list_ranges, soil_list_ranges)
new_fertilizer_ranges = ranges_sort(new_soil_ranges, fertilizer_list_ranges)
new_water_ranges = ranges_sort(new_fertilizer_ranges, water_list_ranges)
new_light_ranges = ranges_sort(new_water_ranges, light_list_ranges)
new_temperature_ranges = ranges_sort(new_light_ranges, temperature_list_ranges)
new_humidity_ranges = ranges_sort(new_temperature_ranges, humidity_list_ranges)
new_location_ranges = ranges_sort(new_humidity_ranges, location_list_ranges)

sorted_location_ranges = sorted(new_location_ranges, key=itemgetter(0))

print("sorted: ", sorted_location_ranges[0])
