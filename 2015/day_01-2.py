import fileinput

directions = input()
floor = 0

direction_number = 0

for direction in directions:
    direction_number += 1

    floor += 1 if direction == '(' else -1
    
    if floor == -1:
        break
    

print('Entered basement with direction {}'.format(direction_number))
