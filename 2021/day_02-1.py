import fileinput

horiz_pos = 0
depth = 0

for line in fileinput.input():
    (direction, magnitude) = line.split()
    magnitude = int(magnitude)

    if direction == 'forward':
        horiz_pos += magnitude
    elif direction == 'down':
        depth += magnitude
    elif direction == 'up':
        depth -= magnitude

print('Final position: {} horizontal, {} depth, {} product'.format(horiz_pos, depth, horiz_pos * depth))
