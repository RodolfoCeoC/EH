# +++ This code is to decrypt encrypted words using shalib +++

import hashlib
import sys


def main():
    welcome = """
Welcome to the password guesser
-------------------------------
This program only decrypts:
MD5 - SHA1 - SHA256 - SHA512
-------------------------------
"""
    print(welcome)
    hash = input("Enter the hash to decrypt"+"\n>> ")
    file = open("words.txt","r")
    list_words = file.read()
    list_words = list_words.split("\n")
    
    if len(hash) == 32: #MD5
        print("The encryption method is MD5")
        print("-"*31)
        
        for i in list_words:
            hash_word = i.encode('utf-8')
            hash_md5 = hashlib.md5(hash_word) ###Check this
            if hash == hash_md5.hexdigest():
                print(f'The word is: {i}')
                break
            else:
                pass

    elif len(hash) == 40: #SHA1
        print("The encryption method is SHA1")
        print("-"*31)
        
        for i in list_words:
            hash_word = i.encode('utf-8')
            hash_sha1 = hashlib.sha1(hash_word)
            if hash == hash_sha1.hexdigest():
                print(f'The word is: {i}')
                break
            else:
                pass

    elif len(hash) == 64: #SHA256
        print("The encryption method is SHA256")
        print("-"*31)
        
        for i in list_words:
            hash_word = i.encode('utf-8')
            hash_sha256 = hashlib.sha256(hash_word)
            if hash == hash_sha256.hexdigest():
                print(f'The word is: {i}')
                break
            else:
                pass
        
    elif len(hash) == 128: #SHA512
        print("The encryption method is SHA512")
        print("-"*31)
        
        for i in list_words:
            hash_word = i.encode('utf-8')
            hash_sha512 = hashlib.sha512(hash_word)
            if hash == hash_sha512.hexdigest():
                print(f'The word is: {i}')
                break
            else:
                pass

    else:
        print("Unrecognized encryption method")
        print("-"*35)



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()