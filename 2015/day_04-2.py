import hashlib

secret_key = input()
answer_found = False

for i in range(1, 100000000):
    combined = '{}{}'.format(secret_key, i)
    combined_hash = hashlib.md5(combined.encode('UTF-8')).hexdigest()

    if combined_hash[0:6] == '000000':
        print('Answer: {}'.format(i))
        answer_found = True
        break

if not answer_found:
    print('Answer not found')
