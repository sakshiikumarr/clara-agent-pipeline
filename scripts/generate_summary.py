import os
import json

ACCOUNTS_FOLDER = "../outputs/accounts"

summary = {
    "total_accounts": 0,
    "accounts": []
}

for account in os.listdir(ACCOUNTS_FOLDER):

    account_path = f"{ACCOUNTS_FOLDER}/{account}"

    versions = os.listdir(account_path)

    summary["accounts"].append({
        "account_id": account,
        "versions": versions
    })

summary["total_accounts"] = len(summary["accounts"])

with open("../outputs/summary.json", "w") as f:
    json.dump(summary, f, indent=2)

print("Pipeline summary generated")