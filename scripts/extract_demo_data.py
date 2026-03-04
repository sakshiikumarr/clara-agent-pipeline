import os
import json
import uuid

with open("../config.json") as f:
    config = json.load(f)

INPUT_FOLDER = "../" + config["demo_dataset"]
OUTPUT_FOLDER = "../" + config["accounts_output"]

def extract_data(transcript):

    data = {
        "account_id": None,
        "company_name": None,
        "business_hours": {},
        "services_supported": [],
        "emergency_definition": [],
        "questions_or_unknowns": []
    }

    text = transcript.lower()

    if "sprinkler" in text:
        data["services_supported"].append("sprinkler services")

    if "alarm" in text:
        data["services_supported"].append("fire alarm services")

    if "9 am" in text:
        data["business_hours"] = {
            "days": "Mon-Fri",
            "start": "9:00",
            "end": "17:00"
        }

    if "8 am" in text:
        data["business_hours"] = {
            "days": "Mon-Fri",
            "start": "8:00",
            "end": "17:00"
        }

    if "emergency" in text:
        data["emergency_definition"].append("system failure or alarm trigger")

    if not data["business_hours"]:
        data["questions_or_unknowns"].append("Business hours not specified")

    if not data["services_supported"]:
        data["questions_or_unknowns"].append("Services supported not specified")

    if not data["emergency_definition"]:
        data["questions_or_unknowns"].append("Emergency definition unclear")
    
    return data


for file in os.listdir(INPUT_FOLDER):

    try:
        with open(f"{INPUT_FOLDER}/{file}") as f:
            transcript = f.read()
    except Exception as e:
        print(f"Error reading file {file}: {e}")
        continue

    account_data = extract_data(transcript)

    account_id = file.replace(".txt", "")
    account_data["account_id"] = account_id

    path = f"{OUTPUT_FOLDER}/{account_id}/v1"

    os.makedirs(path, exist_ok=True)

    with open(f"{path}/memo.json", "w") as f:
        json.dump(account_data, f, indent=2)

print("Demo data processed successfully")