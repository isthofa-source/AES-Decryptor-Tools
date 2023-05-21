# AES-Decryptor-Tools
This is a Python script to decrypt data encrypted by using AES Encryption in CBC (Cipher Block Chaining) mode and PKCS7 padding.

## PoC
![image](https://github.com/isthofa-source/AES-Decryptor-Tools/assets/75401288/cf4418e4-1919-43d4-860a-e281c65c0078)
![image](https://github.com/isthofa-source/AES-Decryptor-Tools/assets/75401288/f15ef0e3-ca9f-4cba-937f-ad8142c71bd5)
![image](https://github.com/isthofa-source/AES-Decryptor-Tools/assets/75401288/3a9a4b0e-6fb6-41fb-8324-11121e234856)

## Requirements
Make sure you have installed the PyCryptodome library before running this script. You can install it using the command:
```py
pip install pycryptodome
```
## Running Test
```py
python AES-DECRYPT.py
```
## Description
PyCryptodome library to **encrypt AES** in **CBC mode**. Then, I used **Crypto.Util.Padding** to remove the **PKCS7 padding** after decrypting the data. The decryption result will be converted into text format using UTF-8 decode before being displayed.

Replace **encrypted_data**, **key**, and **iv** with the appropriate values for your respective cases. Also, note that this example uses AES encryption with a **128-bit (16-byte)** key length. If you use a different key length, adjust it :).

Please remember that encryption and decryption of sensitive data is an important and complex task. Use proper security methods and follow best practices to protect your data :).

Thanks :)

