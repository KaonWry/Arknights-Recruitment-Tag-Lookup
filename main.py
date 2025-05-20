import itertools
import json

with open('operators.json', 'r', encoding='utf-8') as f:
    operators = json.load(f)

input_tags = ['DPS', 'Ranged', 'Top Operator', 'Melee', 'Guard']  # Example input

print(f"Inputted tags: {', '.join(input_tags)}")

def find_operators_by_tags(tag_combo):
    results = []
    for name, info in operators.items():
        if all(tag in info['tags'] for tag in tag_combo):
            results.append(name)
    return results

for n in [3, 2, 1]:
    print(f"\nCombinations of {n} tags:")
    for combo in itertools.combinations(input_tags, n):
        matched = find_operators_by_tags(combo)
        if matched:
            print(f"Tags: {combo} -> Operators: {matched}")