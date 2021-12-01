import fileinput

previous_value = None
times_increased = 0

for line in fileinput.input():
    value = int(line)

    if previous_value is None:
        # This is the first value
        pass
    elif value > previous_value:
        times_increased += 1

    previous_value = value

print('Value increased {} times'.format(times_increased))
