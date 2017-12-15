# http://adventofcode.com/2017/day/10

with open("10_01.in") as f:
    lengths = [ord(c) for c in next(f).strip()]

lengths += [17, 31, 73, 47, 23]

hexcodes = []


# your code goes in here

knot_hash = ''.join("{0:02x}".format(hexcode) for hexcode in hexcodes)

print(knot_hash)
