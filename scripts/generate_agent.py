import os
import json

ACCOUNTS_FOLDER = "../outputs/accounts"


def generate_prompt(data):

    prompt = f"""
You are Clara, an AI receptionist for a service company.

BUSINESS HOURS FLOW
1. Greet the caller politely.
2. Ask the purpose of the call.
3. Collect the caller's name and phone number.
4. Route the call to the appropriate technician.
5. If transfer fails, apologize and record a message.
6. Ask if they need anything else.
7. Close the call politely.

AFTER HOURS FLOW
1. Greet the caller.
2. Ask if the situation is an emergency.
3. If emergency, collect name, phone number, and address immediately.
4. Attempt to transfer the call to the emergency technician.
5. If transfer fails, assure the caller that someone will call back soon.
"""

    return prompt


for account in os.listdir(ACCOUNTS_FOLDER):

    memo_path = f"{ACCOUNTS_FOLDER}/{account}/v1/memo.json"

    with open(memo_path) as f:
        memo = json.load(f)

    agent = {
        "agent_name": f"{account}_agent",
        "voice_style": "professional",
        "version": "v1",
        "system_prompt": generate_prompt(memo),
        "services_supported": memo["services_supported"],
        "business_hours": memo["business_hours"]
    }

    with open(f"{ACCOUNTS_FOLDER}/{account}/v1/agent.json", "w") as f:
        json.dump(agent, f, indent=2)

print("Agent specs generated successfully")