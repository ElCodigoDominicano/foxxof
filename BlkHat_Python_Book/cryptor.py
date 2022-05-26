"""
A simple message in bytes encryption / decryption tool

- uses the asymmetric RSA cipher which uses a public key  / private key technique
- public key usually for encryption and the private for decryption

[!]platform-independent meaning it should work on almost any device...
AERivas
"""
from Cryptodome.Cipher import AES, PKCS1_OAEP
from Cryptodome.PublicKey import RSA
from Cryptodome.Random import get_random_bytes
from io import BytesIO

import base64
import zlib

def generate():
    """
    This function creates 2 files one for the public-key named pub
    and the other file for the private-key named pri
    """
    new_key = RSA.generate(2048)
    private_key = new_key.exportKey()
    public_key = new_key.publickey().exportKey()
    
    with open('key.pri', 'wb') as f:
        f.write(private_key)
    
    with open('key.pub', 'wb') as f:
        f.write(public_key)

def get_rsa_cipher(keytype):
    """
    This function RETURNS the RSA cipher from the generated keys in bytes

    Parameter keytype: the public or private key file (.pub or .pri)
    """
    with open(f'key.{keytype}') as f:
        key = f.read()
    rsakey = RSA.importKey(key)
    return (PKCS1_OAEP.new(rsakey), rsakey.size_in_bytes())

def encrypt(plaintext):
    """
    This function RETURNS  an encrypted string.
    
    a random session key is generated to be used in the AES cipher
    and then is encrypt the compressed text with that cipher
    passed alongside with the session key and the ciphertext so it can be 
    decrypted the session key is added via the RSA key generated from the public key
    information is stored within the payload before the function returns the string

    Parameter plaintext: is in bytes
    """
    compressed_text = zlib.compress(plaintext)

    session_key = get_random_bytes(16)
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(compressed_text)
    
    cipher_rsa = get_rsa_cipher('pub')
    encrypted_session_key = cipher_rsa[0].encrypt(session_key)

    msg_payload = encrypted_session_key + cipher_aes.nonce + tag + ciphertext
    encrypted = base64.encodebytes(msg_payload)
    return(encrypted)


def decrypt(encrypted):
    """
    This function RETURNS the decrypted message.

    Parameter encrypted: the encrypted payload
    """

    encrypted_bytes = BytesIO(base64.decodebytes(encrypted))
    cipher_rsa, keysize_in_bytes = get_rsa_cipher('pri')

    encrypted_session_key = encrypted_bytes.read(keysize_in_bytes)
    nonce = encrypted_bytes.read(16)
    tag = encrypted_bytes.read(16)
    ciphertext = encrypted_bytes.read()

    session_key = cipher_rsa.decrypt(encrypted_session_key)
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    decrypted = cipher_aes.decrypt_and_verify(ciphertext, tag)

    plaintext = zlib.decompress(decrypted)
    return plaintext

if __name__ =='__main__':
    plaintext = b'hey there you'
    print(decrypt(encrypt(plaintext)))