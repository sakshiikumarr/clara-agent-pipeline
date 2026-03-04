import os
import json

with open("../config.json") as f:
    config = json.load(f)

INPUT_FOLDER = "../" + config["onboarding_dataset"]
ACCOUNTS_FOLDER = "../" + config["accounts_output"]

accounts = sorted(os.listdir(ACCOUNTS_FOLDER))
onboarding_files = sorted(os.listdir(INPUT_FOLDER))

count = min(len(accounts), len(onboarding_files))

for i in range(count):

    account_id = accounts[i]
    onboarding_file = onboarding_files[i]

    try:
        with open(f"{INPUT_FOLDER}/{onboarding_file}") as f:
            transcript = f.read().lower()
    except Exception as e:
        print(f"Error reading onboarding file {onboarding_file}: {e}")
        continue

    v1_path = f"{ACCOUNTS_FOLDER}/{account_id}/v1"
    v2_path = f"{ACCOUNTS_FOLDER}/{account_id}/v2"

    os.makedirs(v2_path, exist_ok=True)

    with open(f"{v1_path}/memo.json") as f:
        memo = json.load(f)

    changes = []

    if "timezone" in transcript:
        memo.setdefault("business_hours", {})
        memo["business_hours"]["timezone"] = "EST"
        changes.append("Added timezone from onboarding")

    if "dispatch" in transcript:
        memo["emergency_routing_rules"] = "transfer to dispatch"
        changes.append("Emergency routing updated to dispatch")

    if "technician" in transcript:
        memo["emergency_routing_rules"] = "transfer to on-call technician"
        changes.append("Emergency routing updated to technician")

    with open(f"{v2_path}/memo.json", "w") as f:
        json.dump(memo, f, indent=2)

    changelog = {
        "version_update": "v1 → v2",
        "changes": changes
    }

    with open(f"{v2_path}/changes.json", "w") as f:
        json.dump(changelog, f, indent=2)

print("Onboarding updates processed successfully")