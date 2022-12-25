#This code was created using the nmap3 module

import sys
import time
import nmap3


def os(target,nmap):
    print("-"*50)
    discover_os = nmap.nmap_os_detection(target)
    discover_os = discover_os[target].get('osmatch')
    discover_os = discover_os[0]
    result_so = discover_os.get('name')
    accuracy = discover_os.get('accuracy')
    print("The Operating System is: {} \nThe percentage of accuracy is {}%".format(result_so,accuracy))


def version(target,nmap):
    vers = nmap.nmap_version_detection(target)
    vers = vers.get(target)
    vers = vers.get('ports')

    for i in vers:
        print("-"*50)
        protocol = i.get('protocol')
        port = i.get('portid')
        state = i.get('state')
        service = i.get('service')
        print("Protocol => {}".format(protocol))
        print("Port => {}".format(port))
        print("State => {}".format(state))
        
        for services in service.keys():
            if 'name' in services:
                name = service['name']
                print("Name => {}".format(name))
                
            else:
                name = ""
            
            if 'product' in services:
                product = service['product']
                print("Product => {}".format(product))
                
            else:
                product = ""
            
            if 'version' in services:
                version = service['version']
                print("Version => {}".format(version))
                
            else:
                version = ""
            time.sleep(0.08)


def top_ports(target,nmap):
    print(target)
    top_port = nmap.scan_top_ports(target)
    top_port = top_port.get(target)
    top_port = top_port.get('ports')

    for i in top_port:
        print("-"*20)
        port = i.get('portid')
        service = i.get('service')
        print("Port => {}".format(port))

        for services in service.keys():
            if 'name' in services:
                name = service['name']
                print("Name => {}".format(name))
            else:
                name = ""


def syn_scan(target):
    nmap = nmap3.NmapScanTechniques()
    results = nmap.nmap_syn_scan(target)
    results = results.get(target)
    results = results.get('ports')

    for i in results:
        print("-"*20)
        protocol = i.get('protocol')
        port = i.get('portid')
        state = i.get('state')
        service = i.get('service')
        print("Protocol => {}".format(protocol))
        print("Port => {}".format(port))
        print("State => {}".format(state))

        for services in service.keys():
            if 'name' in services:
                name = service['name']
                print("Name => {}".format(name))
            else:
                name = ""

            if 'method' in services:
                methods = service['method']
                print("Method => {}".format(methods))
            else:
                methods = ""

            if 'conf' in services:
                config = service['conf']
                print("Configuration => {}".format(config))
            else:
                config = ""


def host_discovery(target,nmap):
    print("-"*35)
    host = nmap.nmap_no_portscan(target)
    host = host.get('runtime')
    host = host.get('summary')
    print(host)


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
    number = int(input("Choose a number: "))

    if number != 5:
        target = input("Enter the IP Address: ")
    else:
        pass
    
    nmap = nmap3.Nmap()

    match number:
        case 1: #OS
            os(target,nmap)
        case 2: #Version
            version(target,nmap)
        case 3: #Top Ports
            top_ports(target,nmap)
        case 4: #Syn
            syn_scan(target)
        case _: #Exit
            print("-"*20+"\nBye")
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
    number = int(input("Choose an option: "))
    
    if number == 1:
        switch()
    elif number == 2:
        target = input("Enter the ip address: ")
        nmap = nmap3.NmapHostDiscovery()
        host_discovery(target,nmap)
    else:
        print("-"*20+"\nBye")
        sys.exit()



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()