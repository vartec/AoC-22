from functools import cache
import os

LETTER_TO_NUM_1 = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}

@cache
def score_1(s: str) -> int:
    pair = [LETTER_TO_NUM_1[letter] for letter in s.strip().split(' ')]
    score = pair[1]
    diff = pair[1] - pair[0]
    if diff == 0:
        return score + 3
    if diff%3 == 1:
        return score + 6
    return score

LETTER_TO_NUM_2 = {'A': 1, 'B': 2, 'C': 3, 'X': 0, 'Y': 3, 'Z': 6}

@cache
def score_2(s: str) -> int:
    op_move, result = [LETTER_TO_NUM_2[letter] for letter in s.strip().split(' ')]
    score = result

    if result == 3:
        return score + op_move
    if result == 6:
        return score + op_move%3 + 1
    return score + (op_move + 1)%3 + 1


PATH = os.path.dirname(os.path.abspath(__file__))

total_1 = 0
total_2 = 0
with open(os.path.join(PATH,'input.txt')) as f:
    for line in f:
        total_1 += score_1(line)
        total_2 += score_2(line)

print(f'part 1: {total_1}')
print(f'part 2: {total_2}')