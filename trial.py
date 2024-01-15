from cryptography.fernet import Fernet

# Generate the Keys
key=Fernet.generate_key()
cipher_suite=Fernet(key)

# Text that will be encrypted
original_text = "Merhaba, bu metin şifrelenecek."
cipher_text = cipher_suite.encrypt(original_text.encode())

print(f"Original Text: {original_text}")
print(f"Encrypted Text: {cipher_text}")

# Decoding the Encrypted Text
decrypted_text = cipher_suite.decrypt(cipher_text).decode()
print(f"Decoded Text: {decrypted_text}")