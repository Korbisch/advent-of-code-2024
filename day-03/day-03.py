import re
from typing import Tuple

input = []

with open("./input.txt", 'r') as file:
    input = file.read()

def find_valid_instructions(str) -> list:
    pattern = "mul\([0-9]{1,},[0-9]{1,}\)"
    return re.findall(pattern, str)

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

def calculate_instructions(input):
    valid_instructions = find_valid_instructions(input)
    return execute(valid_instructions)

result = str(calculate_instructions(input))
print(f"Result of mulitplications: {result}")
