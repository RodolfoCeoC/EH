from cryptography.fernet import Fernet
import os

def return_key():
    return open('key.key','rb').read()


def decrypt(items, key):
    i = Fernet(key)
    for item in items:
        with open(item,'rb') as file:
            file_data = file.read()
        data = i.decrypt(file_data)

        with open(item, 'wb') as file:
            file.write(data)

if __name__ == '__main__':
    path = "/home/darkness/Escritorio/importante"
    os.remove(path + "/" + "readme.txt")
    items = os.listdir(path)
    files = [path + "/" + x for x in items]

key = return_key()
decrypt(files, key)