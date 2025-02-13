import json
import bcrypt
from cryptography.fernet import Fernet
import os

ADMIN_FILE = "Hashing\admins.json"
PATIENT_FILE = "patients.json"

# Load admins from file
def load_admins():
    if os.path.exists(ADMIN_FILE):
        with open(ADMIN_FILE, "r") as f:
            return json.load(f)
    return {}

# Encrypt and store patient data
def encrypt_data(key, data):
    f = Fernet(key)
    return f.encrypt(data.encode()).decode()

# Decrypt patient data
def decrypt_data(key, data):
    f = Fernet(key)
    return f.decrypt(data.encode()).decode()

# Load patients
def load_patients():
    if os.path.exists(PATIENT_FILE):
        with open(PATIENT_FILE, "r") as f:
            return json.load(f)
    return []

# Save patients
def save_patients(patients):
    with open(PATIENT_FILE, "w") as f:
        json.dump(patients, f)

# Admin login
def admin_login():
    username = input("Enter admin username: ")
    passcode = input("Enter password: ").encode("utf-8")

    admins = load_admins()

    if username in admins and bcrypt.checkpw(passcode, admins[username].encode("utf-8")):
        print("Login successful!")
        return True
    else:
        print("Admin not found!")
        return False

# Add patient record
def add_patient():
    if not admin_login():
        return
    
    key = Fernet.generate_key()
    f = Fernet(key)

    name = input("Enter patient name: ")
    age = input("Enter age: ")
    email = input("Enter email: ")
    ssn = input("Enter SSN: ")
    history = input("Enter medical history: ")

    encrypted_data = {
        "name": encrypt_data(key, name),
        "age": encrypt_data(key, age),
        "email": encrypt_data(key, email),
        "ssn": encrypt_data(key, ssn),
        "history": encrypt_data(key, history),
        "key": key.decode()
    }

    patients = load_patients()
    patients.append(encrypted_data)
    save_patients(patients)

    print("Patient record added securely!")

# View patient records
def view_patients():
    if not admin_login():
        return

    patients = load_patients()
    
    if not patients:
        print("No patient records found!")
        return
    
    for idx, patient in enumerate(patients):
        key = patient["key"].encode()
        print(f"\nPatient {idx+1}:")
        print("Name:", decrypt_data(key, patient["name"]))
        print("Age:", decrypt_data(key, patient["age"]))
        print("Email:", decrypt_data(key, patient["email"]))
        print("SSN:", decrypt_data(key, patient["ssn"]))
        print("History:", decrypt_data(key, patient["history"]))

# Main loop
while True:
    print("\n1. Admin Login\n2. Add Patient Record\n3. View Patient Records\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        admin_login()
    elif choice == "2":
        add_patient()
    elif choice == "3":
        view_patients()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid option! Try again.")
