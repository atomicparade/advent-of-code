import fileinput

total_sq_ft = 0

for line in fileinput.input():
    parts = line.split('x')
    dims = list(map(int, parts))

    # Get all areas
    areas = [dims[0] * dims[1], dims[0] * dims[2], dims[1] * dims[2]]

    # Slack is equivalent to the smallest area
    slack = min(areas)

    area_required = sum(areas) * 2 + slack

    total_sq_ft += area_required

print('Need {} sq ft of wrapping paper'.format(total_sq_ft))
