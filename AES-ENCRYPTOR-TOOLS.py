from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64

def encrypt_aes_cbc(data, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(data.encode('utf-8'), AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    return encrypted_data

data = "YOUR-DATA"  # Data yang akan dienkripsi
key = b'YOUR-KEY'  # Kunci enkripsi AES 128-bit (16 byte)
iv = b'YOUR-IV'  # Vektor inisialisasi (IV) 16-byte

encrypted_data = encrypt_aes_cbc(data, key, iv)
encrypted_data_base64 = base64.b64encode(encrypted_data).decode('utf-8')

print("Data Terenkripsi:", encrypted_data_base64)
