import hashlib
import rsa

# Generate RSA keys (public & private)
def generate_keys():
    public_key, private_key = rsa.newkeys(2048)
    return public_key, private_key

# Hash the medical report using SHA-256
def hash_report(report_content):
    return hashlib.sha256(report_content.encode()).digest()

# Sign the hash using the doctor's private key
def sign_report(report_content, private_key):
    report_hash = hash_report(report_content)
    signature = rsa.sign(report_hash, private_key, 'SHA-256')
    return signature

# Verify the digital signature
def verify_signature(report_content, signature, public_key):
    try:
        report_hash = hash_report(report_content)
        rsa.verify(report_hash, signature, public_key)
        return True
    except rsa.VerificationError:
        return False

if __name__ == "__main__":
    # Doctor generates keys
    public_key, private_key = generate_keys()

    # Doctor writes a medical report
    report = "Patient John Doe has a stable condition with no major health concerns."
    print("\nDoctor writes a medical report - Patient John Doe has a stable condition with no major health concerns.")

    # Sign the report
    signature = sign_report(report, private_key)
    print("\nDigital Signature Generated:\n", signature.hex())

    # Hospital verifies the report
    print("\nHospital verifies the report")
    is_valid = verify_signature(report, signature, public_key)
    print("\nSignature Verified:    ", is_valid)
