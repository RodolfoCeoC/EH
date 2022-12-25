#This project was made using the nmap3 module

import sys
import time
import nmap3


def os(target,nmap):
    print("-"*50)
    result = nmap.nmap_os_detection(target)
    result = result[target].get('osmatch')
    result = result[0]
    result_so = result.get('name')
    accuracy = result.get('accuracy')
    print("The Operating System is: {} \nThe percentage of accuracy is {}%".format(result_so,accuracy))


def version(target,nmap):

    results = nmap.nmap_version_detection(target)
    results = results.get(target)
    results = results.get('ports')

    for i in results:
        protocol = i.get('protocol')
        port = i.get('portid')
        state = i.get('state')
        service = i.get('service')
        
        for services in service.keys():
            if 'name' in services:
                name = service['name']
                
            else:
                name = "It was not found"
            
            if 'product' in services:
                product = service['product']
                
            else:
                product = "It was not found"
            
            if 'version' in services:
                version = service['version']
                
            else:
                version = "It was not found"     
            
            print("Protocol => {}".format(protocol))
            print("Port => {}".format(port))
            print("State => {}".format(state))
            print("Name => {}".format(name))
            print("Product => {}".format(product))
            print("Version => {}".format(version),"\n"+"-"*50,end="\n")


def switch():
    options = """
Select Scan Type:
[1]. OS Detection
[2]. Service Version Detection
[3]. Top Ports
[4]. Syn Scan
[5]. Exit
"""
    print(options)
    number = 2
    target = "192.168.0.24"#input("Enter the IP Address: ")
    nmap = nmap3.Nmap()

    match number:
        case 1: #OS
            os(target,nmap)
        case 2: #Version
            version(target,nmap)
        case 3: #Top Ports
            pass
        case 4: #Syn
            pass
        case _: #Exit
            print("Bye")
            sys.exit()


def main():
    welcome = """
**Welcome to NMAP!**

Choose an option:
[1]. Scan
[2]. Host Discovery
[3]. Exit
"""
    print(welcome)
    number = 1#int(input("Choose an option: "))
    
    if number == 1:
        switch()
    elif number == 2:
        pass
    else:
        sys.exit()



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()