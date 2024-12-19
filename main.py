import aes

def main():
    folder = aes.read_folder("./dossier_confidentiel")
    aes.encrypt_folder(folder, aes.key)
    aes.decrypt_folder(folder, aes.key)
    print("Hello, World!")

    
if __name__ == "__main__":
    main()