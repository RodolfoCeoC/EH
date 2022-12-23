#Get themes on wordpress

import requests
import time
import sys
from bs4 import BeautifulSoup

list_1 = []
themes_list = []


def main():
    url = input("Ingresa el sitio web: ")
    agent = {'User-Agent':'Firefox'}
    peticion = requests.get(url=url,headers=agent)
    soup = BeautifulSoup(peticion.text, 'html.parser')
    
    for link in soup.find_all('link'):
        if '/wp-content/themes' in link.get('href'):
            href = link.get('href')
            href = href.split('/')
            if 'themes' in href:
                position = href.index('themes')
                theme = href[position + 1]
                list_1.append(theme)
                
    for themes in list_1:
        if themes in themes_list:
            pass
        else:
            themes_list.append(theme)
    
    for themes in themes_list:
        count_themes = themes.index(themes)
        print("Tema {}: {}".format(count_themes + 1,themes))
        time.sleep(1)
            


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit