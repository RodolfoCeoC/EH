import requests
import sys
from os import path


def main():
    if path.exists('wp-plugins.txt'):
        file = open("wp-plugins.txt","r",encoding="utf-8")
        file = file.read().split("\n")
        url = input("Ingresa el link: ")
        
        for plugin in file:
            final_url = url + "/" + plugin
            request = requests.get(url=final_url)
            print("(-) Attempting" + final_url)
            
            if request.status_code == 200:
                print("(+) Succeed" + final_url)
                    
    else:
        print("No se encontró el archivo wp.plugins.txt")



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()