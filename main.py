import itertools
import json
import os
from rapidfuzz import process, fuzz

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

all_tags = sorted({tag for info in operators for tag in info['tags']})
print(f"All available tags: {', '.join(all_tags)}\n")

def fuzzy_select_tags(all_tags, max_tags=5):
    selected = []
    tag_map = {tag.lower(): tag for tag in all_tags}
    all_tags_lower = list(tag_map.keys())
    while len(selected) < max_tags:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"All available tags: {', '.join(all_tags)}\n")
        print(f"Currently selected: {', '.join(selected)}")
        query = input(f"Type to search tags ({len(selected)}/{max_tags} selected, Enter to finish): ").strip().lower()
        if not query:
            break
        matches = process.extract(query, all_tags_lower, scorer=fuzz.WRatio, limit=10)
        if not matches:
            print("No matches found.")
            input("Press Enter to continue...")
            continue
        tag = tag_map[matches[0][0]]
        if tag not in selected:
            selected.append(tag)
            print(f"Added: {tag}")
        else:
            print("Already selected.")
        input("Press Enter to continue...")
    return selected

input_tags = fuzzy_select_tags(all_tags, 5)
if not input_tags:
    print("No tags selected. Exiting.")
    exit()

os.system("cls" if os.name == "nt" else "clear")
print(f"Selected tags: {', '.join(input_tags)}")

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
            # Sort by rarity descending, then by name
            matched.sort(key=lambda x: (-x[1], x[0]))
            print(f"Tags: {', '.join(combo)} -> Operators:\n" +
                  "\n".join(f"- {name} ({rarity}★)" for name, rarity in matched))