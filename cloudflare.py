import sys
import requests


def main():
    website = input("Ingresa el sitio web: ")
    find = "cloudflare"
    url = requests.get(website)
    headers = dict(url.headers)
    verification = False
    for header in headers:
        if find in headers[header].lower():
            verification = True
            break

    if verification == True:
        print("Se encontró Cloudflare en el sitio web")

    else:
        print("No se encontró Cloudflare")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
