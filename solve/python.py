#!/usr/bin/env python3
import hashlib
import sys

prefix = sys.argv[1]
difficulty = int(sys.argv[2])
zeros = '0' * difficulty

def is_valid(digest):
    if sys.version_info.major == 2:
        digest = [ord(i) for i in digest]
    bits = ''.join(bin(i)[2:].zfill(8) for i in digest)
    return bits[:difficulty] == zeros


i = 0
while True:
    i += 1
    s = prefix + str(i)
    h = hashlib.sha256()
    h.update(s.encode())
    if is_valid(h.digest()):
        print(i)
        exit(0)
