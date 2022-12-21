import sys
import requests
import argparse

parser = argparse.ArgumentParser(description="Detector de Cabeceras")
parser.add_argument('-t','--target',help="Objetivo")
parser = parser.parse_args()

def main():
    if parser.target:
        try:
            url = requests.get(url=parser.target)
            cabeceras = dict(url.headers)
            for cabecera in cabeceras:
                print(cabecera + " : " + cabeceras[cabecera])
        except:
            print("Error de conexion")
    else:
        print("No se establecio el objetivo")



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()