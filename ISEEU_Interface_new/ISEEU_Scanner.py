# Scanning Module
import os
import sys
from Hardware_Scan_Module import firmware_check,hash_create
from Network_Scan_Module import packet_sniff, port_check,ftp_check,ssh_check,telnet_check

#from Network_Scan_Module import port_check,ssh_check,ftp_check,telnet_check

def Port_Scan(ip):

    print("\n#####Port Scanning#####")
    print('OPEN PORT : ' + str(port_check.nmap(ip)))

    return port_check.nmap(ip)


def Ftp_Scan(ip):
    print("\033[33m"+"\n####################[FTP port Scanning]########################"+"\033[0m")
    
    portlist = Port_Scan(ip)

    for i in range(0, len(portlist)):
        a = ftp_check.connect(ip, str(portlist[i]))
        #if a == 0:
        #   print(portlist[i], ' : CLOSED PORT')

        #if a == 1:
        #   print(portlist[i], ' : OPEN PORT')
        #   port_info[0] = 1
    # return #ftp_check.connect(ip, port)  # 1 - open, 0 - closed


def Ssh_Scan(ip):
    print("\033[33m"+"\n#####################[SSH port Scanning]#######################"+"\033[0m")
    portlist = Port_Scan(ip)

    for i in range(0, len(portlist)):
        a = ssh_check.connect(ip, str(portlist[i]))

    # return ssh_check.connect(ip, port)  # 1 - open, 0 - closed


def Telnet_Scan(ip):
    print("\033[33m"+"\n###################[Telnet port Scanning]######################"+"\033[0m")
    portlist = Port_Scan(ip)

    for i in range(0, len(portlist)):
        a = telnet_check.connect(ip, str(portlist[i]))

    # return telnet_check.connect(ip, port)   #1 - open, 0 - closed

def Packet_Scan(scan_time):
    print("######################Packet_Scan!#####################")
    packet_sniff.packet_sniff(scan_time)

def Firmware_Scan(path):
    print("######################Firmware_Scan!#####################")
    firmware_check.Check_boot_sequence(path)

def Hash_Create(path):
    print("######################Hash_Create!#####################")
    hash_create.save_hash_dir(path,0)


#print(Ssh_Scan('192.168.175.130'))
#print(Ftp_Scan('192.168.175.130'))
#print(Telnet_Scan('192.168.175.130'))
