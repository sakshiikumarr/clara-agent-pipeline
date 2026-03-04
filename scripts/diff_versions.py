import json
import os

ACCOUNTS_FOLDER = "../outputs/accounts"

for account in os.listdir(ACCOUNTS_FOLDER):

    v1_path = f"{ACCOUNTS_FOLDER}/{account}/v1/memo.json"
    v2_path = f"{ACCOUNTS_FOLDER}/{account}/v2/memo.json"

    if not os.path.exists(v2_path):
        continue

    with open(v1_path) as f:
        v1 = json.load(f)

    with open(v2_path) as f:
        v2 = json.load(f)

    changes = {}

    for key in v2:
        if v1.get(key) != v2.get(key):
            changes[key] = {
                "before": v1.get(key),
                "after": v2.get(key)
            }

    with open(f"{ACCOUNTS_FOLDER}/{account}/v2/diff.json", "w") as f:
        json.dump(changes, f, indent=2)

print("Diff files generated")