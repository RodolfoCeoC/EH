import sys
import requests
from bs4 import BeautifulSoup


def main():
    url = input("Ingresa el sitio web: ")
    header = {'User-Agent':'Firefox'}
    request = requests.get(url=url,headers=header)
    soup = BeautifulSoup(request.text,'html.parser')

    for tag in soup.findAll('meta'):
        if tag.get('name') == 'generator':
            print(tag.get('content'))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()