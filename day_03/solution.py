import os
import string

PRIORITY = {l:p for l,p in zip(string.ascii_letters, range(1, 53))}

def find_dup_1(backpack: str) -> str:
    comp_1, comp_2 = backpack[:len(backpack)//2], backpack[len(backpack)//2:]
    dup = (set(comp_1) & set(comp_2)).pop()
    return dup

def find_dup_2(backpacks: list[str]) -> str:
    dup = (set(backpacks[0]) & set(backpacks[1]) & set(backpacks[2])).pop()
    return dup

PATH = os.path.dirname(os.path.abspath(__file__))

total = 0
with open(os.path.join(PATH,'input.txt')) as f:
    for line in f:
        total += PRIORITY[find_dup_1(line.strip())]

print(f'part 1: {total}')

total = 0
with open(os.path.join(PATH,'input.txt')) as f:
    while f:
        try:
            backpacks = [next(f).strip() for _ in range(3)]
            total += PRIORITY[find_dup_2(backpacks)]
        except StopIteration:
            break

print(f'part 2: {total}')
