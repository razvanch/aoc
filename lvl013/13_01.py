# http://adventofcode.com/2017/day/13
depths = []

with open("tests/01/test01.in", "r") as file:
    for line in file:
        tokens = [int(x) for x in line.strip().split(":")] # transform to int after removing newline and
                                                           # whitespace followed by tokenization using ":" as delimiter
        depths = depths + [(tokens[0], tokens[1])] #create pairs

severity = 0

print(severity)
