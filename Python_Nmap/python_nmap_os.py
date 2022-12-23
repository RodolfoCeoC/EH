import sys
import os

def switch(option):
    match option:
        case '1': #Complete Scan
            nmap_value = " -p- -A"
            return nmap_value
        
        case '2': #Light Scan
            nmap_value = " -T5 --top-ports 10"
            return nmap_value
        
        case '3': #Host Discovery
            nmap_value = " -sn"
            return nmap_value
        
        case '4': #Vulnerability Scan
            nmap_value = " -script vuln"
            return nmap_value
        
        case '5': #OS Scan
            nmap_value = " -O"
            return nmap_value
        
        case '6': #Version Scan
            nmap_value = " -sV"
            return nmap_value
        
        case _: #Exit
            print("See later")
            sys.exit()


def parser(numbers,nmap_query,ip):
    if numbers == '2':
        print("-"*50)
        print(ip)
        results = os.popen(nmap_query).read()
        results = results.split("latency).\n\n")
        print(results[1])
        
    elif numbers == '3':
        print("-"*50)
        print(ip)
        results = os.popen(nmap_query).read()
        results = results.split("address (")
        results = results[1].split(" ho")
        results = results[0]
        
        if results == '1':
            print("The host is active")
        elif results == '0':
            print("The host is down")        
        
    else:    
        print("-"*70)
        print(ip)
        results = os.system(nmap_query)
    

def opt(options,mode,numbers):
    if options == 1:
        print("Enter the Ip")
        target = input(">>")
        query = "nmap " + target + mode
        parser(numbers,query,target)
    else:
        print("Write the name of the .txt file") #You can create your own .txt file
        file = input(">>")
        file = open(file,'r')
        ip_s = file.read().split("\n")
        
        for ip in ip_s:
            query = "nmap " + ip + mode
            parser(numbers,query,ip)
 
        
def main():
    print("\n***Welcome to Automated Nmap***\n"+("-"*31))
    scan_types = """
[1]. Complete Scan
[2]. Light Scan
[3]. Host Discovery
[4]. Vulnerability Scan
[5]. OS Scan
[6]. Version Scan
[7]. Exit
"""
    print(scan_types)
    numbers = input("Type a number: ")
    mode = switch(numbers)
    print("-"*31)
    ip_list = """
[1]. IPV4
[2]. List
""" 
    print(ip_list)
    options = int(input("Select an option: "))
    opt(options,mode,numbers)
    


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()