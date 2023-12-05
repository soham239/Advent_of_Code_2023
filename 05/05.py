file_path = '05.txt'  

lines = []
with open(file_path, 'r') as file:
    
    for line in file:
        lines.append(line)

# Initialize lists
seeds = []
seed_to_soil_map = []
soil_to_fertilizer_map = []
fertilizer_to_water_map = []
water_to_light_map = []
light_to_temperature_map = []
temperature_to_humidity_map = []
humidity_to_location_map = []

# Create a dictionary to map category names to their respective lists
category_map = {
    'seeds': seeds,
    'seed-to-soil map': seed_to_soil_map,
    'soil-to-fertilizer map': soil_to_fertilizer_map,
    'fertilizer-to-water map': fertilizer_to_water_map,
    'water-to-light map': water_to_light_map,
    'light-to-temperature map': light_to_temperature_map,
    'temperature-to-humidity map': temperature_to_humidity_map,
    'humidity-to-location map': humidity_to_location_map,
}

# Parse the input and store in lists
current_category = None

for line in lines:
    # Check if the line contains a category name
    for category in category_map.keys():
        if category in line:
            current_category = category
            # Extract values from the line after the category name
            values = line.split(":")[1].strip()
            if values:
                category_map[current_category] = list(map(int, values.split()))

    # If a category is set, and the line doesn't contain a category name, append the values to the list
    if current_category and not line.startswith(current_category):
        category_map[current_category].append(list(map(int, line.split())))


# Print the lists
# print("Seeds:", category_map['seeds'])
# print("Seed-to-soil map:", seed_to_soil_map)
# print("Soil-to-fertilizer map:", soil_to_fertilizer_map)
# print("Fertilizer-to-water map:", fertilizer_to_water_map)
# print("Water-to-light map:", water_to_light_map)
# print("Light-to-temperature map:", light_to_temperature_map)
# print("Temperature-to-humidity map:", temperature_to_humidity_map)
# print("Humidity-to-location map:", humidity_to_location_map)

for k, v in category_map.items():
    if k != 'seeds':
        category_map[k] =  [(val[1], val[1] + val[2] - 1, val[0]-val[1]) for val in v if val]

def map_value(num, category):
    for start, end, diff in category:
        if start <= num <= end:
            return num + diff
    
    return num

ans = []
for s in category_map['seeds']:
    if s != []:
        # Map one by one
        num = map_value(s, category_map['seed-to-soil map'])
        num = map_value(num, category_map['soil-to-fertilizer map'])
        num = map_value(num, category_map['fertilizer-to-water map'])
        num = map_value(num, category_map['water-to-light map'])
        num = map_value(num, category_map['light-to-temperature map'])
        num = map_value(num, category_map['temperature-to-humidity map'])
        num = map_value(num, category_map['humidity-to-location map'])
        ans.append(num)

print(f"Ans is {min(ans)}")