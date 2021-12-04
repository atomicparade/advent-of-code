import fileinput

# Number of times each bit was on
count_ones = []

for line in fileinput.input():
    line = line.strip()

    if fileinput.lineno() == 1:
        count_ones = [0] * len(line)

    for i in range(len(line)):
        if line[i] == '1':
            count_ones[i] += 1

number_of_readings = fileinput.lineno()

# Gamma = 1 where bit is most frequently on
# Epsilon = 1 where bit is most frequently off

gamma_bits = ''
epsilon_bits = ''

for count in count_ones:
    if count > number_of_readings / 2:
        gamma_bits += '1'
        epsilon_bits += '0'
    else:
        gamma_bits += '0'
        epsilon_bits += '1'

gamma = int(gamma_bits, 2)
epsilon = int(epsilon_bits, 2)

print('Gamma: {}, epsilon: {}, product: {}'.format(gamma, epsilon, gamma * epsilon))
