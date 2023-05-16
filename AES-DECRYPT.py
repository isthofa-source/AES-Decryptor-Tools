from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

def decrypt_aes_cbc(data, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(data)
    unpadded_data = unpad(decrypted_data, AES.block_size)
    return unpadded_data.decode('utf-8')

encrypted_data = "cEIZL9HlDGNhLVrygqnXFg=="  # Data terenkripsi dalam bentuk Base64
key = b'YOUR-KEY'  # Kunci enkripsi AES 128-bit (16 byte)
iv = b'YOUR-IV'  # Vektor inisialisasi (IV) 16-byte

encrypted_data = base64.b64decode(encrypted_data)

decrypted_data = decrypt_aes_cbc(encrypted_data, key, iv)
print("Data Terdekripsi:", decrypted_data)
