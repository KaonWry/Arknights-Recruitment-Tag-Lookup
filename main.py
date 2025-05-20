import itertools

operators = {
    "Ch'en": {
        'rarity': 6,
        'tags': ['Nuker', 'DPS', 'Top Operator', 'Melee', 'Guard']
    },
    'SilverAsh': {
        'rarity': 6,
        'tags': ['Top Operator', 'Melee', 'DPS', 'Support', 'Guard']
    },
    'Skadi': {
        'rarity': 6,
        'tags': ['Top Operator', 'Melee', 'DPS', 'Survival', 'Guard']
    },
    'Helagur': {
        'rarity': 6,
        'tags': ['Top Operator', 'Melee', 'DPS', 'Survival', 'Guard']
    },
    'Blaze': {
        'rarity': 6,
        'tags': ['DPS', 'Survival', 'Top Operator', 'Melee', 'Guard']
    },
    'Thorns': {
        'rarity': 6,
        'tags': ['Top Operator', 'Melee', 'DPS', 'Defense', 'Guard']
    },
    'Surtr': {
        'rarity': 6,
        'tags': ['Top Operator', 'Melee', 'DPS', 'Guard']
    },
    'Aak': {
        'rarity': 6,
        'tags': ['Support', 'DPS', 'Specialist', 'Top Operator', 'Ranged']
    },
    'Bagpipe': {
        'rarity': 6,
        'tags': ['DP-Recovery', 'DPS', 'Melee', 'Top Operator', 'Vanguard']
    },
    'Blemishine': {
        'rarity': 6,
        'tags': ['Defense', 'Healing', 'DPS', 'Top Operator', 'Melee', 'Defender']
    },
    'Ceobe': {
        'rarity': 6,
        'tags': ['DPS', 'Crowd-Control', 'Top Operator', 'Ranged', 'Caster']
    },
    'Eunectes': {
        'rarity': 6,
        'tags': ['DPS', 'Survival', 'Defense', 'Top Operator', 'Melee', 'Defender']
    },
}

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