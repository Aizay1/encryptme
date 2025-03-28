#!/usr/bin/env python3
import argparse
import base64
import binascii
import codecs
import html
import urllib.parse
import sqlite3
import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def print_banner():
    banner = """
    ███████╗███╗   ██╗ ██████╗██████╗ ███████╗███████╗
    ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔════╝  ██║  ██
    █████╗  ██╔██╗ ██║██║     ██████╔╝█████╗    ██║  ██
    ██╔══╝  ██║╚██╗██║██║     ██╔══██╗██╔══╝    ██║  ██
    ███████╗██║ ╚████║╚██████╗██║  ██║███████╗███████╝ 
    ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚══════╝
    
    EncryptMe - Multi-layer Encryption Tool by ZayTech
    """
    print(banner)

# Database Setup
def init_db():
    conn = sqlite3.connect("secure_storage.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS credentials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            encrypted_password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Generate RSA Keys
def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# RSA Encryption
def rsa_encrypt(text, public_key):
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    encrypted = cipher.encrypt(text.encode())
    return base64.b64encode(encrypted).decode()

# RSA Decryption
def rsa_decrypt(text, private_key):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    decrypted = cipher.decrypt(base64.b64decode(text))
    return decrypted.decode()

# Encoding Functions
def hex_encode(text): return text.encode().hex()
def rot13_encode(text): return codecs.encode(text, 'rot_13')
def html_encode(text): return html.escape(text)
def url_encode(text): return urllib.parse.quote(text)
def binary_encode(text): return ' '.join(format(ord(c), '08b') for c in text)
def utf8_encode(text): return text.encode('utf-8').decode('latin1')
def base64_encode(text): return base64.b64encode(text.encode()).decode()

# Decoding Functions
def hex_decode(text): return bytes.fromhex(text).decode()
def rot13_decode(text): return codecs.decode(text, 'rot_13')
def html_decode(text): return html.unescape(text)
def url_decode(text): return urllib.parse.unquote(text)
def binary_decode(text): return ''.join(chr(int(b, 2)) for b in text.split())
def utf8_decode(text): return text.encode('latin1').decode('utf-8')
def base64_decode(text): return base64.b64decode(text).decode()

# Encryption Pipeline
def encrypt(text, public_key):
    return base64_encode(utf8_encode(binary_encode(url_encode(html_encode(rot13_encode(hex_encode(rsa_encrypt(text, public_key))))))))

# Decryption Pipeline
def decrypt(text, private_key):
    return rsa_decrypt(hex_decode(rot13_decode(html_decode(url_decode(binary_decode(utf8_decode(base64_decode(text)))))), private_key))

# CLI Setup
def main():
    print_banner()
    parser = argparse.ArgumentParser(description="EncryptMe CLI - Secure multi-layer encryption tool by ZayTech")
    parser.add_argument("-e", "--encrypt", help="Encrypt a given text")
    parser.add_argument("-d", "--decrypt", help="Decrypt a given encrypted text")
    parser.add_argument("-s", "--store", nargs=2, metavar=("USERNAME", "PASSWORD"), help="Store encrypted credentials")
    parser.add_argument("-r", "--retrieve", help="Retrieve and decrypt stored password by username")
    args = parser.parse_args()
    
    private_key, public_key = generate_keys()
    init_db()
    
    if args.encrypt:
        print("Encrypted text:", encrypt(args.encrypt, public_key))
    elif args.decrypt:
        print("Decrypted text:", decrypt(args.decrypt, private_key))
    elif args.store:
        store_credentials(args.store[0], args.store[1], public_key)
        print("Credentials stored successfully!")
    elif args.retrieve:
        decrypted = retrieve_credentials(args.retrieve, private_key)
        if decrypted:
            print("Decrypted Password:", decrypted)
        else:
            print("Username not found.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

