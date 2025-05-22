import itertools
import json
import random

with open('operators.json', 'r', encoding='utf-8') as f:
    operators = json.load(f)  

for info in operators:
    if info.get("rarity") == 6:
        info["tags"].append("Top Operator")
    if info.get("rarity") == 5:
        info["tags"].append("Senior Operator")
    if info.get("rarity") == 2:
        info["tags"].append("Starter")
    if info.get("rarity") == 1:
        info["tags"].append("Robot")

all_tags = set()
for info in operators:
    all_tags.update(info['tags'])
all_tags = sorted(all_tags)
print(f"All available tags: {', '.join(all_tags)}\n")

input_tags = random.sample(all_tags, 5)

print(f"Inputted tags: {', '.join(input_tags)}")

def find_operators_by_tags(tag_combo):
    results = []
    for info in operators:
        if info.get("rarity") == 6 and "Top Operator" not in tag_combo:
            continue
        if all(tag in info['tags'] for tag in tag_combo):
            results.append((info['name'], info['rarity']))
    return results

for n in [3, 2, 1]:
    print(f"\nCombinations of {n} tags:")
    for combo in itertools.combinations(input_tags, n):
        matched = find_operators_by_tags(combo)
        if matched:
            print(f"Tags: {', '.join(combo)} -> Operators:\n" +
                  "\n".join(f"- {name} ({rarity}★)" for name, rarity in matched))