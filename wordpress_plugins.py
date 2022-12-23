import requests
import sys
import time
from bs4 import BeautifulSoup

plugin_list = []
final_list = []


def main():
    url = input("Ingresa el sitio web: ")
    agent = {'User-Agent':'Firefox'}
    petition = requests.get(url=url,headers=agent)
    soup = BeautifulSoup(petition.text,'html.parser')
    
    for link in soup.find_all('link'):
        if 'wp-content/plugins' in link.get('href'):
            href = link.get('href')
            href = href.split('/')
            position = href.index('plugins')
            plugin = href[position + 1]
            plugin_list.append(plugin)
    
    for plugins in plugin_list:
        if plugins in final_list:
            pass
        
        else:
            final_list.append(plugins)
            
    for plugins in final_list:
        print("(+) Se encontró el plugin {}".format(plugins))
        time.sleep(0.5)



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()