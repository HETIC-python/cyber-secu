import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

EXTENSIONS_FILE = "extensions.txt"

def encrypt_file(input_file, output_file, key):
    with open(input_file, "rb") as f:
        data = f.read()
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(data, AES.block_size))
    with open(output_file, "wb") as f:
        f.write(cipher.iv + ciphertext)

def decrypt_file(input_file, output_file, key):
    with open(input_file, "rb") as f:
        data = f.read()
    iv = data[:16]
    ciphertext = data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    with open(output_file, "wb") as f:
        f.write(plaintext)

def encrypt_folder(input_folder, output_folder, key):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(EXTENSIONS_FILE, "w") as ext_file:
        for root, _, files in os.walk(input_folder):
            for file in files:
                input_file = os.path.join(root, file)
                relative_path = os.path.relpath(input_file, input_folder)
                file_name, file_ext = os.path.splitext(relative_path)
                encrypted_path = file_name + ".enc"
                output_file = os.path.join(output_folder, encrypted_path)

                ext_file.write(f"{file_name}: {file_ext}\n")

                os.makedirs(os.path.dirname(output_file), exist_ok=True)

                encrypt_file(input_file, output_file, key)
                print(f"Encrypting: '{input_file}' to '{output_file}'")

def decrypt_folder(input_folder, output_folder, key):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    extensions = {}
    with open(EXTENSIONS_FILE, "r") as ext_file:
        for line in ext_file:
            original_path, file_ext = line.strip().split(": ")
            extensions[original_path] = file_ext

    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".enc"):
                input_file = os.path.join(root, file)
                relative_path = os.path.relpath(input_file, input_folder)
                file_name = relative_path[:-4]
                file_ext = extensions.get(file_name, "")
                output_file = os.path.join(output_folder, file_name + file_ext)

                os.makedirs(os.path.dirname(output_file), exist_ok=True)

                decrypt_file(input_file, output_file, key)
                print(f"Decrypting: '{input_file}' to '{output_file}'")

with open("key.bin", "wb") as f:
    key = get_random_bytes(32)
    f.write(key)

input_folder = "dossier_confidentiel"
encrypted_folder = "dossier_crypté"
decrypted_folder = "dossier_décrypté"

print("=== Starting Encryption ===")
encrypt_folder(input_folder, encrypted_folder, key)

with open("key.bin", "rb") as f:
    loaded_key = f.read()

print("\n=== Starting Decryption ===")
decrypt_folder(encrypted_folder, decrypted_folder, loaded_key)
