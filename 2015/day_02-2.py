import fileinput

total_ft = 0

def list_product(list):
    product = 1

    for item in list:
        product *= item

    return product

for line in fileinput.input():
    parts = line.split('x')
    dims = list(map(int, parts))

    longest_side = max(dims)
    remainder = sum(dims) - longest_side
    wrapping_ft_required = remainder * 2
    
    bow_ft_required = list_product(dims)
    total_ft += wrapping_ft_required + bow_ft_required

print('Need {} ft of ribbon'.format(total_ft))
