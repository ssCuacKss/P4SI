import argparse
import json
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

parser = argparse.ArgumentParser(description='Descifra un fichero que contiene un json en AES a texto')

parser.add_argument("entrada",help="el nombre del fichero a desencriptar", type=str)

args= parser.parse_args()



inputKey = input("enter the key: ")

try:
    key= bytes.fromhex(inputKey) 

except (ValueError, KeyError):
    print("numero introducido no hexadecimal")
    exit()

try:
    with open(args.entrada) as file:
        b64 = json.load(file)
        
    initvec = b64decode(b64['iv'])
    content = b64decode(b64['ciphertext'])
    cipher = AES.new(key, AES.MODE_CBC, initvec)
    decmsg = unpad(cipher.decrypt(content), AES.block_size)
    print("\nThe message was: ", decmsg)

except (ValueError, KeyError):
    print("Incorrect decryption")
