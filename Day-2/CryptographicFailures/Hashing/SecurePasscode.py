import bcrypt
import json
import os

ADMIN_FILE = "admins.json"

# Load admins from file
def load_admins():
    if os.path.exists(ADMIN_FILE):
        with open(ADMIN_FILE, "r") as f:
            return json.load(f)
    return {}

# Save admins to file
def save_admins(admins):
    with open(ADMIN_FILE, "w") as f:
        json.dump(admins, f)

# Register admin
def register():
    username = input("Enter a username: ")
    passcode = input("Enter a passcode: ").encode("utf-8")
    salt = bcrypt.gensalt(rounds=15)
    hashed_passcode = bcrypt.hashpw(passcode, salt)

    admins = load_admins()
    admins[username] = hashed_passcode.decode("utf-8")
    save_admins(admins)

    print("Registration successful!")

# Login admin
def login():
    username = input("Enter username: ")
    passcode = input("Enter passcode: ").encode("utf-8")

    admins = load_admins()

    if username in admins and bcrypt.checkpw(passcode, admins[username].encode("utf-8")):
        print("Login successful! Access granted.")
        return True
    else:
        print("Invalid credentials!")
        return False

# Main loop
while True:
    print("\n1. Register\n2. Login\n3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid option! Try again.")
