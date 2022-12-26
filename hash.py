#This code is to encrypt words using hashlib

import hashlib
import sys


def md5(word):
    encrypt_md5 = hashlib.md5(word)
    encrypt_md5 = encrypt_md5.hexdigest()
    print("-"*len(encrypt_md5)+"\n"+encrypt_md5)


def sha1(word):
    encrypt_sha1 = hashlib.sha1(word)
    encrypt_sha1 = encrypt_sha1.hexdigest()
    print("-"*len(encrypt_sha1)+"\n"+encrypt_sha1)


def sha256(word):
    encrypt_sha256 = hashlib.sha256(word)
    encrypt_sha256 = encrypt_sha256.hexdigest()
    print("-"*len(encrypt_sha256)+"\n"+encrypt_sha256)


def sha512(word):
    encrypt_sha512 = hashlib.sha512(word)
    encrypt_sha512 = encrypt_sha512.hexdigest()
    print("-"*len(encrypt_sha512)+"\n"+encrypt_sha512)


def main():
    options = """
Encryptor

[1]. MD5
[2]. SHA1
[3]. SHA256
[4]. SHA512
[5]. Exit
"""
    print(options)
    select = int(input("Select an option: "))
    word = input("Enter the words: ")
    word = word.encode('utf-8')
    
    match select:
        case 1:
            md5(word)
        case 2:
            sha1(word)
        case 3:
            sha256(word)
        case 4:
            sha512(word)
        case _:
            sys.exit()



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()