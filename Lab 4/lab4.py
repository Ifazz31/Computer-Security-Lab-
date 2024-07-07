import argparse
import hashlib
import time
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Signature import pkcs1_15
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import SHA256

def create_symmetric_key(size, output_file):
    secret = get_random_bytes(size)
    with open(output_file, 'wb') as f:
        f.write(secret)
    print(f"Symmetric key of length {size * 8} bits created and saved to {output_file}")

def create_asymmetric_keypair(key_size, private_output, public_output):
    keypair = RSA.generate(key_size)
    private = keypair.export_key()
    public = keypair.publickey().export_key()
    
    with open(private_output, 'wb') as f:
        f.write(private)
    with open(public_output, 'wb') as f:
        f.write(public)
    print(f"Asymmetric key pair of {key_size} bits created and saved to {private_output} and {public_output}")

def symmetric_crypt(input_file, key_file, cipher_mode, action, output_file):
    with open(key_file, 'rb') as f:
        secret = f.read()

    cipher = AES.new(secret, cipher_mode)
    if action == 'encrypt':
        with open(input_file, 'rb') as f:
            content = f.read()
        padded_content = pad(content, AES.block_size)
        encrypted = cipher.encrypt(padded_content)
        with open(output_file, 'wb') as f:
            f.write(encrypted)
    elif action == 'decrypt':
        with open(input_file, 'rb') as f:
            encrypted = f.read()
        padded_content = cipher.decrypt(encrypted)
        content = unpad(padded_content, AES.block_size)
        with open(output_file, 'wb') as f:
            f.write(content)
        print(content.decode())

def asymmetric_crypt(input_file, key_file, action, output_file):
    with open(key_file, 'rb') as f:
        key = RSA.import_key(f.read())

    cipher = PKCS1_OAEP.new(key)
    if action == 'encrypt':
        with open(input_file, 'rb') as f:
            content = f.read()
        encrypted = cipher.encrypt(content)
        with open(output_file, 'wb') as f:
            f.write(encrypted)
    elif action == 'decrypt':
        with open(input_file, 'rb') as f:
            encrypted = f.read()
        content = cipher.decrypt(encrypted)
        with open(output_file, 'wb') as f:
            f.write(content)
        print(content.decode())

def digital_signature(input_file, key_file, action, sig_output):
    with open(key_file, 'rb') as f:
        key = RSA.import_key(f.read())

    with open(input_file, 'rb') as f:
        content = f.read()

    if action == 'sign':
        hash_obj = SHA256.new(content)
        signature = pkcs1_15.new(key).sign(hash_obj)
        with open(sig_output, 'wb') as f:
            f.write(signature)
    elif action == 'verify':
        with open(sig_output, 'rb') as f:
            signature = f.read()
        hash_obj = SHA256.new(content)
        try:
            pkcs1_15.new(key).verify(hash_obj, signature)
            print("Signature is valid.")
        except (ValueError, TypeError):
            print("Signature is not valid.")

def compute_hash(input_file):
    with open(input_file, 'rb') as f:
        content = f.read()
    hash_obj = hashlib.sha256(content)
    print(hash_obj.hexdigest())

def main():
    parser = argparse.ArgumentParser(description="Cryptographic Operations")
    parser.add_argument('operation', choices=['create_sym_key', 'create_asym_key', 'sym_encrypt', 'sym_decrypt', 'asym_encrypt', 'asym_decrypt', 'sign', 'verify', 'hash'], help='Cryptographic operation to perform')
    parser.add_argument('input_file', nargs='?', help='Path to the input file')
    parser.add_argument('--key_file', help='Path to the key file', required=False)
    parser.add_argument('--mode', choices=['ECB', 'CFB'], help='Mode for symmetric encryption', required=False)
    parser.add_argument('--output', help='Path to the output file', required=False)
    parser.add_argument('--sig_file', help='Path to the signature file', required=False)
    parser.add_argument('--size', type=int, choices=[16, 32], help='Size of symmetric key (in bytes)', required=False)
    parser.add_argument('--private_key', help='Path to save the private key', required=False)
    parser.add_argument('--public_key', help='Path to save the public key', required=False)
    parser.add_argument('--key_size', type=int, help='Bit length for asymmetric key', required=False)
    args = parser.parse_args()

    start = time.time()
    
    if args.operation == 'create_sym_key':
        create_symmetric_key(args.size, args.key_file)
    elif args.operation == 'create_asym_key':
        create_asymmetric_keypair(args.key_size, args.private_key, args.public_key)
    elif args.operation == 'sym_encrypt':
        symmetric_crypt(args.input_file, args.key_file, AES.MODE_ECB if args.mode == 'ECB' else AES.MODE_CFB, 'encrypt', args.output)
    elif args.operation == 'sym_decrypt':
        symmetric_crypt(args.input_file, args.key_file, AES.MODE_ECB if args.mode == 'ECB' else AES.MODE_CFB, 'decrypt', args.output)
    elif args.operation == 'asym_encrypt':
        asymmetric_crypt(args.input_file, args.key_file, 'encrypt', args.output)
    elif args.operation == 'asym_decrypt':
        asymmetric_crypt(args.input_file, args.key_file, 'decrypt', args.output)
    elif args.operation == 'sign':
        digital_signature(args.input_file, args.key_file, 'sign', args.sig_file)
    elif args.operation == 'verify':
        digital_signature(args.input_file, args.key_file, 'verify', args.sig_file)
    elif args.operation == 'hash':
        compute_hash(args.input_file)

    end = time.time()
    duration = end - start
    print(f"Time taken for {args.operation}: {duration:.6f} seconds")

if __name__ == "__main__":
    main()
