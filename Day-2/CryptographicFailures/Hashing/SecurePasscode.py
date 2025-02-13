import bcrypt

# In-memory database to store user credentials
users_db = {}

def hash_passcode(passcode):
    """Securely hash the passcode using bcrypt."""
    salt = bcrypt.gensalt()
    hashed_passcode = bcrypt.hashpw(passcode.encode(), salt)
    return hashed_passcode

def register_user():
    """Register a new admin with a securely hashed passcode."""
    username = input("Enter a username: ").strip()
    
    if username in users_db:
        print("Username already exists. Choose a different one.")
        return
    
    passcode = input("Enter a passcode: ").strip()
    hashed_passcode = hash_passcode(passcode)
    
    # Store in the in-memory database
    users_db[username] = hashed_passcode
    print("Registration successful!")

def verify_login(username, passcode):
    """Verify user login by checking hashed passcode."""
    if username not in users_db:
        return False
    
    hashed_passcode = users_db[username]
    return bcrypt.checkpw(passcode.encode(), hashed_passcode)

def login_user():
    """Allow the admin to log in securely."""
    attempts = 3
    
    while attempts > 0:
        username = input("Enter username: ").strip()
        passcode = input("Enter passcode: ").strip()
        
        if verify_login(username, passcode):
            print("Login successful! Access granted.")
            return True
        else:
            attempts -= 1
            print(f"Login failed! Attempts left: {attempts}")
    
    print("Too many failed attempts. Account locked.")
    return False

def main():
    """Main menu to choose registration or login."""
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
