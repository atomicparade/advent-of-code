directions = input()

houses = {}
x = 0
y = 0

def visit_house(x, y):
    if (x, y) not in houses:
        houses[(x, y)] = 0

    houses[(x, y)] += 1

for direction in directions:
    visit_house(x, y)

    if direction == '<':
        x -= 1
    if direction == '>':
        x += 1
    if direction == '^':
        y -= 1
    if direction == 'v':
        y += 1

    visit_house(x, y)

print('Visited {} houses'.format(len(houses)))
