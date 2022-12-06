from collections import deque
from advent.util import * # noqa

input = next(get_input_lines())

for part, n in [(1, 4),(2, 14)]:
    head, tail = deque(input[:n]), deque(input[n:])
    for i in range(n, len(input)+1):
        if len(set(head)) == n:
            print(f"part {part}: {i}")
            break
        head.popleft()
        head.append(tail.popleft())
