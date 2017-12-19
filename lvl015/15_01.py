gen_a_factor = 16807
gen_b_factor = 48271

test_file = "tests/01/test01.in"
input_file = "input.txt"

with open(test_file, "r") as file:
    gen_a_seed = int(file.readline().strip().split()[-1])
    gen_b_seed = int(file.readline().strip().split()[-1])

# your code goes here
