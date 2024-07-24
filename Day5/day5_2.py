input = "input5_1"

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

# New seed list
new_seed_list = []
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
        new_seed_list.append(
            list(range(int(seed_start_point), int(seed) + int(seed_start_point)))
        )
        seed_loop_counter = 0

# print(new_seed_list)

# The way I did it above, it makes a list of lists. This list is made to combine them so we have 1 list of numbers
all_together_seed_list = []

# Loop to add the lists together to make one long list of numbers
for seed_list in new_seed_list:
    all_together_seed_list += seed_list

# print(all_together_seed_list)

# Take all the seeds and test them against the soil map. If its in the offset portion then add it to the list
# if it isn't then add the seed number to the result list as it is unchanged.
for seed in all_together_seed_list:
    is_it_offset = False
    for maps in seed_to_soil_maps:
        # print(maps.split())
        splitnums = maps.split()
        if int(seed) >= int(splitnums[1]) and int(seed) <= (
            int(splitnums[1]) + (int(splitnums[2]) - 1)
        ):
            difference = int(splitnums[0]) - int(splitnums[1])
            result = int(seed) + difference
            is_it_offset = True
            seed_to_soil_R.append(result)
    if not is_it_offset:
        seed_to_soil_R.append(seed)

# print("Soil:")
# print(seed_to_soil_R)

for soil in seed_to_soil_R:
    is_it_offset = False
    for maps in soil_to_fertilizer_maps:
        # print(maps.split())
        splitnums = maps.split()
        if int(soil) >= int(splitnums[1]) and int(soil) <= (
            int(splitnums[1]) + (int(splitnums[2]) - 1)
        ):
            difference = int(splitnums[0]) - int(splitnums[1])
            result = int(soil) + difference
            is_it_offset = True
            soil_to_fertilizer_R.append(result)
    if not is_it_offset:
        soil_to_fertilizer_R.append(soil)

# print("Fertilizer:")
# print(soil_to_fertilizer_R)

# Take fertilizer results which is 4 times
for fertilizer in soil_to_fertilizer_R:
    # Set flag for offset check
    is_it_offset = False
    # Take maps in this case 4 - loop is going 4 times I've checked.
    for maps in fertilizer_to_water_maps:
        # Split the map so I have individual numbers. Print the current map
        # print(maps.split())
        splitnums = maps.split()
        # If my fertilizer number is >= the source and my fertilizer number <= source + (range-1) as it is zero indexed.
        # THEN do the map stuff.
        if int(fertilizer) >= int(splitnums[1]) and int(fertilizer) <= (
            int(splitnums[1]) + (int(splitnums[2]) - 1)
        ):
            # Find the difference between source and destination.
            difference = int(splitnums[0]) - int(splitnums[1])
            # Add the difference to the fertilizer number (it might add a negative which is correct)
            result = int(fertilizer) + difference
            # Set the offset flag to true
            is_it_offset = True
            # Append to the water result list
            fertilizer_to_water_R.append(result)
    # If there is no offset then the number is unchanged. Append it to the water result list.
    if not is_it_offset:
        fertilizer_to_water_R.append(fertilizer)

# print("Water:")
# print(fertilizer_to_water_R)

for water in fertilizer_to_water_R:
    is_it_offset = False
    for maps in water_to_light_maps:
        # print(maps.split())
        splitnums = maps.split()
        if int(water) >= int(splitnums[1]) and int(water) <= (
            int(splitnums[1]) + (int(splitnums[2]) - 1)
        ):
            difference = int(splitnums[0]) - int(splitnums[1])
            result = int(water) + difference
            is_it_offset = True
            water_to_light_R.append(result)
    if not is_it_offset:
        water_to_light_R.append(water)

# print("Light:")
# print(water_to_light_R)

for light in water_to_light_R:
    is_it_offset = False
    for maps in light_to_temperature_maps:
        # print(maps.split())
        splitnums = maps.split()
        if int(light) >= int(splitnums[1]) and int(light) <= (
            int(splitnums[1]) + (int(splitnums[2]) - 1)
        ):
            difference = int(splitnums[0]) - int(splitnums[1])
            result = int(light) + difference
            is_it_offset = True
            light_to_temperature_R.append(result)
    if not is_it_offset:
        light_to_temperature_R.append(light)

# print("Temperature:")
# print(light_to_temperature_R)

for temperature in light_to_temperature_R:
    is_it_offset = False
    for maps in temperature_to_humidity_maps:
        # print(maps.split())
        splitnums = maps.split()
        if int(temperature) >= int(splitnums[1]) and int(temperature) <= (
            int(splitnums[1]) + (int(splitnums[2]) - 1)
        ):
            difference = int(splitnums[0]) - int(splitnums[1])
            result = int(temperature) + difference
            is_it_offset = True
            temperature_to_humidity_R.append(result)
    if not is_it_offset:
        temperature_to_humidity_R.append(temperature)

# print("Humidity:")
# print(temperature_to_humidity_R)

for humidity in temperature_to_humidity_R:
    is_it_offset = False
    for maps in humidity_to_location_maps:
        # print(maps.split())
        splitnums = maps.split()
        if int(humidity) >= int(splitnums[1]) and int(humidity) <= (
            int(splitnums[1]) + (int(splitnums[2]) - 1)
        ):
            difference = int(splitnums[0]) - int(splitnums[1])
            result = int(humidity) + difference
            is_it_offset = True
            humidity_to_location_R.append(result)
    if not is_it_offset:
        humidity_to_location_R.append(humidity)

# print("Location:")
# print(humidity_to_location_R)

# Sort list to get the lowest location
humidity_to_location_R.sort()
print(humidity_to_location_R[0])
