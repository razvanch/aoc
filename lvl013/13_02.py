depths = []

with open("input.txt", "r") as file:
    for line in file:
        tokens = [int(x) for x in line.strip().split(":")] # transform to int after removing newline and
                                                           # whitespace followed by tokenization using ":" as delimiter
        depths = depths + [(tokens[0], tokens[1])] #create pairs

