import string

from advent.util import * # noqa

PRIORITY = {l:p for l,p in zip(string.ascii_letters, range(1, 53))}

def find_dup_1(backpack: str) -> str:
    comp_1, comp_2 = backpack[:len(backpack)//2], backpack[len(backpack)//2:]
    dup = (set(comp_1) & set(comp_2)).pop()
    return dup

def find_dup_2(backpacks: list[str]) -> str:
    dup = (set(backpacks[0]) & set(backpacks[1]) & set(backpacks[2])).pop()
    return dup

part_1_total = sum(PRIORITY[find_dup_1(line.strip())] for line in get_input_lines())
part_2_total = sum(PRIORITY[find_dup_2(backpacks)] for backpacks in get_input_chunks_by_size(3))

print(f'part 1: {part_1_total}')
print(f'part 2: {part_2_total}')
