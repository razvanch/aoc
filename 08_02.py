# http://adventofcode.com/2017/day/8

from collections import namedtuple


Expression = namedtuple(
    "Expression",
    [
        "register",
        "operator",
        "value",
        "condition_register",
        "condition_operator",
        "condition_value"
    ]
)


expressions = []

with open("08_01.in") as f:
    for line in f:
        tokens = line.split()

        # "value" and "conditon_value" fields
        for index in (2, 6):
            tokens[index] = int(tokens[index])

        # remove the "if" token
        tokens.pop(3)

        expressions.append(Expression(*tokens))


max_register = 0

# your code goes in here

print(max_register)
