# Script para simular el modo IPS de Suricata en Freebsd

import sys
import subprocess
import re
import time
import os

ip_result = []
ip_firewall = []

LOGFILE = "/var/log/suricata/fast.log"
PF = "/etc/pf.conf"


def reiniciar_pf():
    reiniciar_pf = f"service pf restart" # Reiniciamos el servicio de packet filter
    subprocess.run(reiniciar_pf, shell=True, check=True)


def main():
    while True:
        file = open(LOGFILE,"r")
        logs = file.read()
        logs = logs.replace(" ", "")
        logs = logs.split()

        for i in logs:
            if "Drop" in i:
                direccion_ip = re.search('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', i)
                result = direccion_ip.group(0)
                ip_result.append(result) # Mandamos el resultado de los logs a una lista
                #print(result)

        # Verificamos si el archivo pf.conf tiene datos existentes

        if os.path.getsize(PF) == 0:
            conjunto = set(ip_result)
            no_rep = list(conjunto)
            print("El archivo pf.conf está vacio. Enviando direcciones ip nuevas")

            for ip_res in no_rep:
                print(f"La dirección ip {ip_res} fue bloqueada")
                time.sleep(1)
                preparar_ip = f"block in from {ip_res}"
                enviar_ip = f"echo {preparar_ip} >> /etc/pf.conf"
                subprocess.run(enviar_ip, shell=True, check=True)

            reiniciar_pf()

        else:
            with open(PF, 'r') as fw_pf: #Abrimos el archivo pf.conf de freebsd
                contenido = fw_pf.read()
                contenido = contenido.replace(" ", "")
                contenido = contenido.split()

                for j in contenido:
                    block_firewall = re.search('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', j)
                    block_firewall = block_firewall.group(0)
                    #print(block_firewall)
                    ip_firewall.append(block_firewall) # Mandamos los resultados del firewall a una lista                

            # Comparamos si hay resultados repetidos en ambas listas
            elementos_no_repetidos = list(set(ip_result) ^ set(ip_firewall))
            
            if not elementos_no_repetidos:
                print("No hay direcciones ip nuevas")
            
            else:
                pass

                for ip in elementos_no_repetidos:
                    print(f"La dirección ip {ip} fue bloqueada")
                    time.sleep(1)
                    resultado = f"block in from {ip}"
                    ip_maliciosa = f"echo {resultado} >> /etc/pf.conf"
                    subprocess.run(ip_maliciosa, shell=True, check=True)
        
                reiniciar_pf()
                
            time.sleep(10)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()