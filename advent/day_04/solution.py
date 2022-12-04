from typing import NamedTuple

from advent.util import * # noqa

class Assignement(NamedTuple):
    start: int
    end: int

def parse_line(line: str):
    start_1, end_1, start_2, end_2 = (int(x) for x in line.replace('-',',').split(','))
    return Assignement(start_1, end_1), Assignement(start_2, end_2)

def fully_contained(line: str) -> int:
    assignements = parse_line(line)
    if assignements[0].start <= assignements[1].start and assignements[0].end >= assignements[1].end:
        return 1
    if assignements[1].start <= assignements[0].start and assignements[1].end >= assignements[0].end:
        return 1
    return 0

def overlapping(line: str) -> int:
    assignements = parse_line(line)

    if assignements[0].start > assignements[1].end:
        return 0
    if assignements[1].start > assignements[0].end:
        return 0
    return 1

result_part_1 = sum(fully_contained(line) for line in get_input_lines())
result_part_2 = sum(overlapping(line) for line in get_input_lines())

print(f'part 1: {result_part_1}')
print(f'part 2: {result_part_2}')