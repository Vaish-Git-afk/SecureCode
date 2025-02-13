from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import os

# File paths
PRIVATE_KEY_FILE = "private_key.pem"
PUBLIC_KEY_FILE = "public_key.pem"
ENCRYPTED_FILE = "encrypted_data.bin"

# Step 1: Generate RSA Key Pair
def generate_keys():
    if not os.path.exists(PRIVATE_KEY_FILE) or not os.path.exists(PUBLIC_KEY_FILE):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        public_key = private_key.public_key()

        # Save private key
        with open(PRIVATE_KEY_FILE, "wb") as f:
            f.write(private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            ))

        # Save public key
        with open(PUBLIC_KEY_FILE, "wb") as f:
            f.write(public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))

        print("RSA key pair generated and saved.")

# Step 2: Encrypt patient data with the doctor's public key
def encrypt_data(patient_data):
    with open(PUBLIC_KEY_FILE, "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    encrypted = public_key.encrypt(
        patient_data.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    with open(ENCRYPTED_FILE, "wb") as f:
        f.write(encrypted)

    print("Patient data encrypted and saved.")

# Step 3: Doctor decrypts data using private key
def decrypt_data():
    with open(PRIVATE_KEY_FILE, "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

    with open(ENCRYPTED_FILE, "rb") as f:
        encrypted_data = f.read()

    decrypted = private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    print("Decrypted Patient Data:", decrypted.decode())

# Menu
def main():
    generate_keys()
    while True:
        print("\n1. Encrypt Patient Data")
        print("2. Decrypt Data (Doctor)")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            patient_data = input("Enter patient data: ")
            encrypt_data(patient_data)
        elif choice == "2":
            decrypt_data()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()