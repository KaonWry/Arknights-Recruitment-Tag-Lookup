# Arknights Recruitment Tag Searcher

A simple Python script to help you find Arknights operators based on recruitment tag combinations.

## How it works

- Loads operator data from `operators.json`.
- Enter up to 5 tags in `main.py`.
- The script prints all operator matches for every combination of 3, 2, and 1 tags (just like how is it in the game).

## Usage

1. Place the operator data in `operators.json`.
2. Edit `input_tags` in `main.py` with your desired tags. (TODO: add a fzf-like functon to search for tags)
3. Run the script:

   ```
   python main.py
   ```

##