import heapq

max_calories = [0, 0, 0]
current_calories = 0

with open('./input.txt') as f:
    for line in f:
        if line.strip():
            current_calories += int(line)
        else:
            heapq.heappushpop(max_calories, current_calories)
            current_calories = 0
heapq.heappushpop(max_calories, current_calories)

print(f"part 1: {sorted(max_calories)[-1]}")
print(f"part 2: {sum(max_calories)}")