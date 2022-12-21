import json
from base64 import b64encode
import argparse
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

parser = argparse.ArgumentParser(description='Cifra un fichero de texto en AES')

parser.add_argument("entrada",help="el nombre del fichero a encriptar", type=str)

args= parser.parse_args()


with (open(args.entrada,"r")) as file:
     data = bytes(file.read(),'utf-8')


key = get_random_bytes(16)

cipher = AES.new(key, AES.MODE_CBC)
content_bytes = cipher.encrypt(pad(data, AES.block_size))

initvec = b64encode(cipher.iv).decode('utf-8')
content = b64encode(content_bytes).decode('utf-8')

result = {}

result["iv"] = initvec
result["ciphertext"]= content

print(result)

print("key = {}".format(key.hex()))

with open('fileData.json', 'w') as fileout:
    json.dump(result, fileout)
