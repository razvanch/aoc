gen_a_factor = (16807, 4) # added modulus check to status as tuple
gen_b_factor = (48271, 8) # added modulus check to status as tuple
test_file = "tests/01/test01.in"
input_file = "input.txt"

with open(input_file, "r") as file:
    gen_a_seed = int(file.readline().strip().split()[-1])
    gen_b_seed = int(file.readline().strip().split()[-1])

# your code goes here
