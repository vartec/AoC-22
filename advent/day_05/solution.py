from copy import deepcopy
from advent.util import * # noqa

def parse_stacks(stack_lines: list[str]) -> dict[str: list[str]]:
    stacks = {i.strip():list() for i in stack_lines.pop().split()}
    for line in reversed(stack_lines):
        # this assumes Py3.6+, where every dict is an OrderedDict preserving key order
        for (key, chunk) in zip(stacks.keys(), zip(*[iter(line)] * 4)):
            crate = chunk[1]
            if crate != ' ':
                stacks[key].append(crate)
    return stacks

def parse_move(line: str) -> tuple:
    parts = line.split()
    return int(parts[1]), parts[3], parts[5]


stack_lines = []
with get_input_file() as f:
    for line in f:
        if line == '\n':
            break
        stack_lines.append(line)

    stacks_1 = parse_stacks(stack_lines)
    stacks_2 = deepcopy(stacks_1)

    for line in f:
        how_many, move_from, move_to = parse_move(line)
        stacks_1[move_to].extend(reversed(stacks_1[move_from][-1*how_many:]))
        del stacks_1[move_from][-1*how_many:]
        stacks_2[move_to].extend(stacks_2[move_from][-1*how_many:])
        del stacks_2[move_from][-1*how_many:]

result_1 = ''.join(s.pop() for s in stacks_1.values())
result_2 = ''.join(s.pop() for s in stacks_2.values())

print(f'part 1: {result_1}')
print(f'part 2: {result_2}')