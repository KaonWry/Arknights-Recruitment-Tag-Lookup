import itertools
import json

with open('operators.json', 'r', encoding='utf-8') as f:
    operators = json.load(f)

# Add tags to operators based on their rarity
for info in operators.values():
    if info.get("rarity") == 6:
        info["tags"].append("Top Operator")
    if info.get("rarity") == 5:
        info["tags"].append("Senior Operator")
    if info.get("rarity") == 2:
        info["tags"].append("Starter")
    if info.get("rarity") == 1:
        info["tags"].append("Robot")

all_tags = set()
for info in operators.values():
    all_tags.update(info['tags'])
all_tags = sorted(all_tags)
print(f"All available tags: {', '.join(all_tags)}\n")

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
            print(f"Tags: {', '.join(combo)} -> Operators:\n" + "\n".join(f"- {name}" for name in matched))