import subprocess
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target', help = "Escribe el sitio web Ejemplo http://google.com")
parser = parser.parse_args()

def main():
    if parser.target:
        subprocess.run("py -m wad -u" + parser.target + "> technologies.txt",shell=True)
        file = open("technologies.txt","r")
        technologies = file.read()
        technologies = technologies.split("[")
        technologies = technologies[1].split("]")
        technologies = technologies[0]
        technologies = technologies.split("{")

        for technologie in technologies:
            new = technologie.replace('\n','')
            new = new.replace('            ','')
            new = new.replace('"','')
            new = new.split('}')
            new = new[0]
            new = new.replace(',','\n')
            print(new)
            print("-"*50)
    else:
        print("No ingreso el sitio web")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()

