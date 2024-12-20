from Crypto.Cipher import AES
import encryption.aes as aes

def restore_files_in_directory(directory,key):
    folder = aes.read_folder(directory)
    aes.decrypt_folder(folder,aes.key ) 

if __name__ == "__main__":
    try:
        restore_files_in_directory("./dossier_confidentiel")
    except ValueError as e:
        print(f"[ERROR] Clé invalide : {e}")
        exit(1)
