import random
import string

pw = ''

pw_len = input('Enter how long the password: ')
pw_len = int(pw_len)

for i in range(pw_len):
    pw += random.choice(string.printable)

print(f'Here you go: {pw}')
