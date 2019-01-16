# Scanning Module
import os
import sys
#from Hardware_Scan_Module import firmware_check
import port_check
import ftp_check
import ssh_check
import telnet_check

ip = '192.168.175.130'
#port_info = [0,0,0,0]

def Port_Scan(ip):
    #print(port_check.nmap(ip))
    print("Port_Scan!")
    return port_check.nmap(ip)

def Ftp_Scan(ip):
    
    print("FTP Scan!")
    #Port_Scan(ip) # list
    portlist = Port_Scan(ip)
    
    for i in range(0, len(portlist)):
        a = ftp_check.connect(ip, str(portlist[i]))
        if a == 0:  
            print(portlist[i],' : CLOSED PORT')

        if a == 1:
            print(portlist[i],' : OPEN PORT')
            port_info[0] = 1
    #return #ftp_check.connect(ip, port)  # 1 - open, 0 - closed

def Ssh_Scan(ip):
    print("SSH_Scan!")
    portlist = Port_Scan(ip)
    
    for i in range(0, len(portlist)):
        a = ssh_check.connect(ip, str(portlist[i]))
        if a == 0 :
            print(portlist[i], ' : CLOSED PORT')

        if a == 1 :
            print(portlist[i], ' : OPEN PORT')
            port_info[1] = 1

    #return ssh_check.connect(ip, port)  # 1 - open, 0 - closed

def Telnet_Scan(ip, port):
    print("Telnet_Scan!")
    return telnet_check.connect(ip, port)   #1 - open, 0 - closed

def Http_Scan():
    print("HTTP_SCAN!")

def Packet_Scan():
    print("Packet_SCAN!")

def Backdoor_Scan():
    print("Backdoor_SCAN!")

def Firmware_Scan(Path):
    firmware_check.Check_boot_sequence(Path)


#print(Port_Scan('192.168.175.130'))
Ssh_Scan('192.168.175.130') #1 = open, 0 = closed

#print(Ssh_Scan('192.168.175.130','22')) 
#print(Telnet_Scan('192.168.175.130','22'))
