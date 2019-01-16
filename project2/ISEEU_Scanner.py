# Scanning Module
import os
import sys
#from Hardware_Scan_Module import firmware_check
import port_check
import ftp_check
import ssh_check
import telnet_check

def Port_Scan(ip):
    #print(port_check.nmap(ip))
    print("Port_Scan!")
    return port_check.nmap(ip)

def Ftp_Scan(ip, port):
    print("FTP_Scan!")
    return ftp_check.connect(ip, port)  # 1 - open, 0 - closed

def Ssh_Scan(ip, port):
    print("SSH_Scan!")
    return ssh_check.connect(ip, port)  # 1 - open, 0 - closed

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
#print(Ftp_Scan('192.168.175.130','21')) #1 = open, 0 = closed
#print(Ssh_Scan('192.168.175.130','22')) 
#print(Telnet_Scan('192.168.175.130','22'))
