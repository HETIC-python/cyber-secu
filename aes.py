from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import os

# key = get_random_bytes(32)
key = "bonjourbonjourbonjourbonjourbonj"
# print(key)

def encrypt_msg(msg, key):
    key = key.encode()
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(msg.encode(), AES.block_size))
    return b"".join([cipher.iv, ciphertext])

def decrypt_msg(text, key):
    print("before encode: ", key)
    key = key.encode()
    print("after encode: ", key)
    iv = text[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(text[16:]), AES.block_size).decode()
    return plaintext

def read_folder(path):
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))
    return files

def encrypt_folder(folder, key):
    for file in folder:
        with open(file, "r") as f:
            data = f.read()
        with open(file, "bw") as f:
            f.write(encrypt_msg(data, key))

def decrypt_folder(folder, key):
    for file in folder:
        with open(file, "br") as f:
            data = f.read()
        print("data", data)
        with open(file, "w") as f:
            f.write(decrypt_msg(data, key))
    
if __name__ == "__main__":
    folder = read_folder("/tmp/test")
    encrypt_folder(folder, key)
    decrypt_folder(folder, key)
    print(folder)
    folder = read_folder("/tmp/test")
    # encrypt_folder(folder, key)
    decrypt_folder(folder, key)
    print(folder)


# print(key)
# msg = "hello paul the goat"
# ciphertext = encrypt_msg(msg, key)
# print("MESSAGE CHIFFRE: ", ciphertext)
#
# with open("./message.enc", "w") as m:
#     m.write(ciphertext)
#
# with open("./key.bin", "w") as k:
#     k.write(key)


# with open("./ciphered.enc", "br") as f:
#     data = f.read()
# with open("./key.bin", "rb") as f:
#     key = f.read()

# #key = "39bd86cbb946593404399edfc5ae2d4149d4f0b2c0ffd700cd16b099ab8d09ca"
# decrypted = decrypt_message(data, key)
# print(decrypted)

# print(decrypt_message(encrypt_msg("jiad", key), key))
