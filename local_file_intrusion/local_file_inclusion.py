import sys
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',help="Enter the URL with possible vulnerability (example) https://website.com/?parameter=")
parser = parser.parse_args()


def main():
    file = open("payload_lfi.txt","r")
    file = file.read().split("\n")
    agent = {'User-Agent':'Firefox'}
    
    if parser.target:
        print("Execution will start in {}".format(parser.target))
        print("-"*50)

        for payload in file:
            consult = requests.get(url=parser.target + payload,headers=agent)

            if 'root' in consult.text:
                print("-"*50)
                print("Probably LFI {}".format(parser.target + payload))
            else:
                pass



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()