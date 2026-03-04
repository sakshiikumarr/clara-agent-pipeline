import os
import json

ACCOUNTS_FOLDER = "../outputs/accounts"

tasks = []

for account in os.listdir(ACCOUNTS_FOLDER):

    tasks.append({
        "account_id": account,
        "task": "Review generated agent configuration",
        "status": "pending"
    })

with open("../outputs/tasks.json", "w") as f:
    json.dump(tasks, f, indent=2)

print("Task tracker created")