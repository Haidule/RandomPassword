digits = '0123456789'

chars = 'abcdefghijklmn' \
    'opqrstuvwxyz'

up = chars.upper()
special = '_!$%&?'
all = digits+chars+up+special
from random import choice

password = ''.join(
    choice(all) for i in range(10)
)

print(password)