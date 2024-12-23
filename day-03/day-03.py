import re
from typing import Tuple
from tkinter.constants import FALSE

input = []

with open("./input.txt", 'r') as file:
    input = file.read()

mul_pattern = r'mul\([0-9]{1,},[0-9]{1,}\)'

def find_valid_instructions(str) -> list:
    return re.findall(mul_pattern, str)

def execute(instructions) -> int:
    result = 0
    for instruction in instructions:
        val1, val2 = split(instruction)
        result += val1 * val2
    return result

def split(instruction) -> Tuple:
    lst = instruction.split(',')
    val1 = lst[0].replace('mul(', '')
    val2 = lst[1].replace(')', '')
    return (int(val1), int(val2))

def calculate_instructions(input) -> int:
    valid_instructions = find_valid_instructions(input)
    return execute(valid_instructions)

result = str(calculate_instructions(input))
print(f"Result of mulitplications: {result}")

# Part 2
# find next: instruction, start or stop and append to array
# remove everything from don't() to do()
do_pattern = r"do\(\)"
dont_pattern = r"don\'t\(\)"

def combine_patterns(p1, p2, p3):
    return re.compile("(%s|%s|%s)" % (p1, p2, p3))

def calculate_enabled(input):
    combined = combine_patterns(mul_pattern, do_pattern, dont_pattern)
    instructions = re.findall(combined, input)
    instructions = remove_disabled(instructions)
    return execute(instructions)

def remove_disabled(instructions):
    result = []
    valid = True
    for instruction in instructions:
        if instruction == "do()":
            valid = True
            continue
        elif instruction == "don't()":
            valid = False
            continue
        elif instruction.startswith("mul") and valid:
            result.append(instruction)

    return result

result = str(calculate_enabled(input))
print(f"Result of enabled instructions: {result}")
