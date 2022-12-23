import socket
import sys
from datetime import datetime

ports = []

def main():
    target = input("Ingresa la IP: ")
    
    print("-"*50)
    print("Target: " + target)
    print("Inicio de escaneo: " + str(datetime.now()))
    print("-"*50)
    
    for port in range(22, 30):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        
        if result == 0:
            ports.append(port)
            print("Puerto {} abierto".format(port))
            
            
        else:
            print("El puerto {} está cerrado".format(port))
        s.close()
        
    print(f'\nHay {len(ports)} puertos abiertos, los cuales son:\n')
    
    for p in ports:
        print("(*)Puerto: {}".format(p))
        



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()