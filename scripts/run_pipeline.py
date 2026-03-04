import os
from datetime import datetime

def log(message):
    print(f"[{datetime.now()}] {message}")

log("Starting pipeline")

log("Running demo extraction...")
os.system("python extract_demo_data.py")

log("Generating agent configurations...")
os.system("python generate_agent.py")

log("Applying onboarding updates...")
os.system("python update_onboarding.py")

log("Generating version diffs...")
os.system("python diff_versions.py")

log("Generating pipeline summary...")
os.system("python generate_summary.py")

log("Creating task tracker...")
os.system("python create_tasks.py")

log("Pipeline completed successfully")