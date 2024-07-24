input = "check_input"

# Open the input file and read it line by line.
with open(input, "r") as f:
    lines = f.read().splitlines()

# Get seeds from the list.
seed_list_with_title = lines[0].split()

# Strip out the title.
seed_list = seed_list_with_title[1:]
# print(seed_list)

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


# print(seed_to_soil_maps)
# print(soil_to_fertilizer_maps)
# print(fertilizer_to_water_maps)
# print(water_to_light_maps)
# print(light_to_temperature_maps)
# print(temperature_to_humidity_maps)
# print(humidity_to_location_maps)

# Result lists
seed_to_soil_R = []
soil_to_fertilizer_R = []
fertilizer_to_water_R = []
water_to_light_R = []
light_to_temperature_R = []
temperature_to_humidity_R = []
humidity_to_location_R = []

# Seed list ranges
seed_list_ranges = []
# Counter to keep track of if its 0 which equals the start number or 1 which equals the range of numbers
seed_loop_counter = 0
# Loop to get the new seed ranges
for seed in seed_list:
    # If the counter is 0 then its a start point
    if seed_loop_counter == 0:
        # Save the start point number
        seed_start_point = seed
        # Increment the counter
        seed_loop_counter += 1
        # If the counter is 1 then its a range
    elif seed_loop_counter == 1:
        # Append the new list with all the numbers from the start point to the end of the range.
        seed_end_point = seed_start_point + seed
        seed_loop_counter = 0
        seed_list_ranges.append([seed_start_point, seed_end_point])

print(seed_list_ranges)
