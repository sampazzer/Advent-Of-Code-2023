input = "check_input"

# Open the input file and read it line by line.
with open(input, "r") as f:
    lines = f.read().splitlines()

# Get seeds from the list.
seed_list_with_title = lines[0].split()

# Strip out the title.
seed_list = seed_list_with_title[1:]
print(seed_list)

# Seed to soil maps:
seed_to_soil_maps = lines[3:5]

# Soil to fertilizer maps:
soil_to_fertilizer_maps = lines[7:10]

# Fertilizer to water maps:
fertilizer_to_water_maps = lines[12:16]

# Water to light maps:
water_to_light_maps = lines[18:20]

# Light to temperature maps:
light_to_temperature_maps = lines[22:25]

# Temperture to humidity maps:
temperature_to_humidity_maps = lines[27:29]

# Humidity to location maps:
humidity_to_location_maps = lines[31:33]


# print(seed_to_soil_maps)
# print(soil_to_fertilizer_maps)
# print(fertilizer_to_water_maps)
# print(water_to_light_maps)
# print(light_to_temperature_maps)
# print(temperature_to_humidity_maps)
# print(humidity_to_location_maps)
