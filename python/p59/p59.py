# http://projecteuler.net/problem=59
import itertools
import string

def apply_xor(ciphertext, key):
    return [c ^ key[i % len(key)] for i, c in enumerate(ciphertext)]

def is_probably_english(letters):
    return 'the' in {word.lower() for word in letters.split()}

ciphertext = map(int, open('cipher1.txt').read().split(','))
keys = (map(ord, key) for key in itertools.permutations(string.lowercase, 3))

for key in keys:
    plaintext = ''.join(map(chr, apply_xor(ciphertext, key)))
    if is_probably_english(plaintext):
        print sum(map(ord, plaintext))
        break
