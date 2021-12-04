import fileinput

def get_most_common_value(values, bit_position):
    count_ones = len(list(filter(lambda value: value[bit_position] == '1', values)))
    return '1' if count_ones >= len(values) / 2 else '0' # If count is equal, return 1

readings = []

for line in fileinput.input():
    value = line.strip()
    readings.append(value)

number_of_bits = len(readings[0])

o2_generator_rating_values = readings
co2_scrubber_rating_values = readings

for i in range(number_of_bits):
    if len(o2_generator_rating_values) > 1:
        o2_generator_rating_most_common_value = get_most_common_value(o2_generator_rating_values, i)
        o2_generator_rating_values = list(filter(
            lambda value: value[i] == o2_generator_rating_most_common_value, # Keep the most common bit
            o2_generator_rating_values
        ))

    if len(co2_scrubber_rating_values) > 1:
        co2_scrubber_rating_most_common_value = get_most_common_value(co2_scrubber_rating_values, i)
        co2_scrubber_rating_values = list(filter(
            lambda value: value[i] != co2_scrubber_rating_most_common_value, # Keep the least common bit
            co2_scrubber_rating_values
        ))

    if len(o2_generator_rating_values) == 1 and len(co2_scrubber_rating_values) == 1:
        break

o2_generator_rating = int(o2_generator_rating_values[0], 2)
co2_scrubber_rating = int(co2_scrubber_rating_values[0], 2)

print('O2 generator rating: {}, CO2 scrubber rating: {}, product: {}'.format(
    o2_generator_rating,
    co2_scrubber_rating,
    o2_generator_rating * co2_scrubber_rating
))
