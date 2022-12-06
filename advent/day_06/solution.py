from advent.util import * # noqa

input = next(get_input_lines())

for part, n in [(1, 4),(2, 14)]:
    for i in range(len(input)-n):
        # Because of slicing this is O(n²) solution, which is good enough for AoC.
        # This can be done in O(n) by using collections.deque
        if len(set(input[i:i+n])) == n:
            print(f"part {part}: {i+n}")
            break
