import fileinput

directions = input()
floor = 0

for direction in directions:
    floor += 1 if direction == '(' else -1

print('Go to floor {}'.format(floor))
