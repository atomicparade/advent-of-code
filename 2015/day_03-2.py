class Santa:
    def __init__(self):
        self.x = 0
        self.y = 0

houses = {}
human_santa = Santa()
robo_santa = Santa()
human_santas_turn = True

def visit_house(x, y):
    if (x, y) not in houses:
        houses[(x, y)] = 0

    houses[(x, y)] += 1

directions = input()

for direction in directions:
    santa = human_santa if human_santas_turn else robo_santa

    visit_house(santa.x, santa.y)

    if direction == '<':
        santa.x -= 1
    if direction == '>':
        santa.x += 1
    if direction == '^':
        santa.y -= 1
    if direction == 'v':
        santa.y += 1

    visit_house(santa.x, santa.y)

    human_santas_turn = not human_santas_turn

print('Visited {} houses'.format(len(houses)))
