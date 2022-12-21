#ENCRYPTION (encAESclassic.py)
import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

data = b"secret"
data += b" word" # podríamos añadiendo datos a encriptar

key = get_random_bytes(16)

cipher = AES.new(key, AES.MODE_CBC)
ct_bytes = cipher.encrypt(pad(data, AES.block_size))

# Se ha creado un cipher.iv aleatorio.
# cipher.iv y ct_bytes son 'bytes'
# Podemos almacenar ct_bytes y cipher.iv como queramos
# Pero en este ejemplo usaremos el formato JSON
# Pero JSON no admite bytes, solo str
# b64encode() codifica en Base64 y de ahí a str no hay problema
# Si no pasamos antes a Base64, podría darnos problemas en JSON.

iv = b64encode(cipher.iv).decode('utf-8')
ct = b64encode(ct_bytes).decode('utf-8')

result = {}

result["iv"] = iv
result["ciphertext"]= ct

print(result)

print("key = {}".format(key.hex()))

with open('data.json', 'w') as outfile:
    json.dump(result, outfile)

print("bye.")