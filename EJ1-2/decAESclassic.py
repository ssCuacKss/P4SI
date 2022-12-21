#DECRYPTION (decAESclassic.py)
import json
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# We assume that the key was securely shared beforehand
i = input("enter the key: ")

try:
    key= bytes.fromhex(i) #bytes de un srt hexadecimal

except (ValueError, KeyError):
    print("You entered a non-hexadecimal number")
    exit()

try:
    with open("data.json") as json_data:
        b64 = json.load(json_data)
        print(b64)
    iv = b64decode(b64['iv'])
    ct = b64decode(b64['ciphertext'])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    print("The message was: ", pt)

except (ValueError, KeyError):
    print("Incorrect decryption")