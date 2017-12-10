# http://adventofcode.com/2017/day/7

from collections import defaultdict, namedtuple
import re


Program = namedtuple("Program", ["name", "weight", "subprogram_names"])

programs = {}

compiled = re.compile(r"(?P<name>[a-z]+) \((?P<weight>[0-9]+)\)( -> (?P<subprogram_names>[a-z]+(, [a-z]+)*))?")


with open("07_01.in") as f:
    for line in f:
        extracted = compiled.match(line).groupdict()

        name = extracted["name"]
        weight = int(extracted["weight"])

        subprogram_names = (
            extracted["subprogram_names"].split(", ")
            if extracted["subprogram_names"]
            else []
        )

        programs[name] = Program(name, weight, subprogram_names)
        

fixed_weight = 0

# your code goes in here

print(fixed_weight)
