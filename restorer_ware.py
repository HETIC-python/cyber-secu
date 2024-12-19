from Crypto.Cipher import AES
import os

def decrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as f:
            iv = f.read(16)
            encrypted_data = f.read()

        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = cipher.decrypt(encrypted_data)

        # Suppression du padding
        padding_length = decrypted_data[-1]
        decrypted_data = decrypted_data[:-padding_length]

        # Sauvegarde dufichier déchiffré
        decrypted_file_path = file_path.replace('.enc', '')
        with open(decrypted_file_path, 'wb') as f:
            f.write(decrypted_data)

        # Suppression du fichier chiffré
        os.remove(file_path)

        print(f"[SUCCESS] Fichier restauré : {decrypted_file_path}")
    except Exception as e:
        print(f"[ERROR] Impossible de déchiffrer {file_path} : {e}")

def restore_files_in_directory(directory, key):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.enc'): 
                file_path = os.path.join(root, file_name)
                decrypt_file(file_path, key)

if __name__ == "__main__":
    key_hex = input("Entrez la clé de déchiffrement (hexadécimal) : ")
    try:
        key = bytes.fromhex(key_hex)
        if len(key) != 32:
            raise ValueError("La clé doit être de 256 bits (64 caractères hexadécimaux).")
    except ValueError as e:
        print(f"[ERROR] Clé invalide : {e}")
        exit(1)

    restore_files_in_directory("./dossier_confidentiel", key)