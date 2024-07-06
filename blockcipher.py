import os
import struct
from Crypto.Cipher import AES

# Define the AES block size in bytes (128 bits)
BLOCK_SIZE = 16

def encrypt_ecb(plaintext, key):
    # TODO: Implement ECB encryption mode using AES-128 and the given key

    ciphertext = b'' 
    return ciphertext

def encrypt_cbc(plaintext, key, iv):
    # TODO: Implement CBC encryption mode using AES-128, the given key, and IV
    # for 
    ciphertext = b'' 
    return ciphertext

def encrypt_file(input_file, output_file, key, iv=None, mode='ecb'):
    with open(input_file, 'rb') as f:
        bmp_header = f.read(14)
        dib_header = f.read(40)

        data = f.read()

    # Add padding to the data if necessary to make it a multiple of the block size
    data += b'\x00' * (BLOCK_SIZE - (len(data) % BLOCK_SIZE))
    print(data);

    # Encrypt the data using the specified mode
    if mode == 'ecb':
        ciphertext = encrypt_ecb(data, key)
    elif mode == 'cbc':
        if iv is None:
            iv = os.urandom(BLOCK_SIZE) # Generate a random IV if none is provided
        ciphertext = encrypt_cbc(data, key, iv)

    # Write the encrypted BMP file header, DIB header, IV (if using CBC mode), and ciphertext to the output file
    with open(output_file, 'wb') as f:
        f.write(bmp_header)
        f.write(dib_header)
        if mode == 'cbc':
            f.write(iv)
        f.write(ciphertext)

key = os.urandom(BLOCK_SIZE) # Generate a random key
input_file = 'input.bmp'
output_file_ecb = 'output_ecb.bmp'
output_file_cbc = 'output_cbc.bmp'
encrypt_file(input_file, output_file_ecb, key, mode='ecb')
encrypt_file(input_file, output_file_cbc, key, mode='cbc')
