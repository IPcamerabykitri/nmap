import os
import pexpect 


def Port_Scan(ip):
    print("Port_Scan!")

    num = []

    command = "nmap -F "+ip
    process = os.popen(command)
    results = str(process.read())
    r = results.split()
    del r[0:28:1]
    del r[-12:-1:1]
    r.pop()

    for group in chunker(r,3):  
        #print(group)           #check for nmap_result
        if group[1] == 'open':
            i = int(re.findall('\d+', group[0][0]))      #Print only Number
            num.append(i)       #i is open_port

    return num

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


def Ftp_Scan(ip, port):
    print("FTP_Scan!")

    connStr = 'ftp '+ip+' '+port
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.EOF, 'Name .*:', \
            '[P|p]assword:', pexpect.TIMEOUT], timeout=10)

    try :
        if ret == 0 :
            #print('[-] Error connecting')
            a = 0
            return a
        if ret == 1 :
            #print('[+] This is FTP Service')
            a = 1
            return a
        if ret == 2 :
            #print('[+] This is FTP Service..')
            a = 1
            return a
        else :
            a = 0
            return a
    except pexpect.EOF :
        print 'EOF@!!'

    chlid.close()
    return a


def Ssh_Scan():

    print("SSH_Scan!")

def Telnet_Scan(ip, port):
    print("Telnet_Scan!")

    connStr = 'telnet '+host+' '+num



def Http_Scan():
    print("HTTP_SCAN!")

def Packet_Scan():
    print("Packet_SCAN!")

def Backdoor_Scan():
    print("Backdoor_SCAN!")

def Firmware_Scan():
    print("Firmware_SCAN!")
