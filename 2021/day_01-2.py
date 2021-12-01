import fileinput

values = []
previous_sum = None
times_increased = 0

for line in fileinput.input():
    value = int(line)

    values.append(value)

    if len(values) == 3:
        this_sum = sum(values)

        if previous_sum is not None:
            if this_sum > previous_sum:
                times_increased += 1

        previous_sum = this_sum
        values.pop(0)

print('Value increased {} times'.format(times_increased))
