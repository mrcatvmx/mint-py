import os
import json
import time
import subprocess

def clone_repository():
    subprocess.run(["git", "clone", "https://github.com/muzammilvmx/Mintforest-bot"])

def install_dependencies():
    os.chdir("Mintforest-bot")
    subprocess.run(["npm", "install"])

def configure_accounts():
    accounts = []
    multiple_accounts = input("Do you want to configure multiple accounts? (yes/no): ").lower() == "yes"
    while True:
        api_token = input("Paste your MintChain API token: ").strip()
        accounts.append(f"Bearer {api_token}")
        if not multiple_accounts or input("Do you want to add another account? (yes/no): ").lower() != "yes":
            break
    with open("accounts.json", "w") as f:
        json.dump(accounts, f)

def schedule_task(interval):
    print(f"Bot is scheduled to run every {interval // 3600} hours.")
    while True:
        print(f"\nNext run in {interval // 3600} hours.")
        subprocess.run(["npm", "start"])
        time.sleep(interval)

def main():
    clone_repository()
    install_dependencies()
    configure_accounts()
    interval = 24 * 60 * 60  # 24 hours in seconds
    schedule_task(interval)

if __name__ == "__main__":
    main()
