from Crypto.Cipher import AES
import aes

def restore_files_in_directory(directory,key="bonjourbonjourbonjourbonjourbonj"):
    print("key: ", key, aes.key)
    folder = aes.read_folder(directory)
    aes.decrypt_folder(folder,key ) # paul add arg key

if __name__ == "__main__":
    try:
        restore_files_in_directory("./dossier_confidentiel")
    except ValueError as e:
        print(f"[ERROR] Clé invalide : {e}")
        exit(1)
