import os
import argparse
import re
import ssh_check
import ftp_check
import telnet_check

###print only number### i = int(re.findall('\d+',s)[0])

def nmap(ip):
    num = []

    command = "nmap -F "+ip
    process = os.popen(command)
    results = str(process.read())
    r = results.split()
    del r[0:28:1]
    del r[-12:-1:1]
    r.pop()

    for group in chunker(r, 3):
        #print(group) ### check for nmap result
        
        if group[1] == 'open':
            i = int(re.findall('\d+', group[0])[0])     # print only number
            num.append(i)                            # i is open port
            
    return num

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--ip", help="python prac.py -i <target IP>", required=True)
    args = parser.parse_args()
    ip_a = args.ip

    #print(type(nmap(ip_a)))   ### type : list

    info_port = [0,0,0,0]  # [ftp, ssh, telnet, http] information... 0-closed, 1-open

    #INPUT SUCCESS#
    if args.ip:
        
        print(' [*] OPEN PORT : ', nmap(ip_a))         #print open port list
         
        ##error test## print(ssh_check.connect('root', ip_a, str(nmap(ip_a)[0])))

#CHECK SSH PORT# SUCCESS HAHA
#        for i in range(0,len(nmap(ip_a))):
#            if ssh_check.connect('root', ip_a, str(nmap(ip_a)[i])) == 0 :
#                print(nmap(ip_a)[i],'is not SSH port')
#            if ssh_check.connect('root', ip_a, str(nmap(ip_a)[i])) == 1 :
#                print(nmap(ip_a)[i],'is SSH port!!')
#                info_port[1] = 1
#
#            print(info_port)

#CHECK FTP PORT.. SUCCESS        
#        for i in range(0,len(nmap(ip_a))):
#            if ftp_check.connect(ip_a, str(nmap(ip_a)[i])) == 0 :
#                print(nmap(ip_a)[i], 'is not FTP port!')
#
#            if ftp_check.connect(ip_a, str(nmap(ip_a)[i])) == 1 :
#                print(nmap(ip_a)[i], 'is FTP port!')
#                info_port[0] = 1


#CHECK TELNET PORT 
        for i in range(0,len(nmap(ip_a))):
            if telnet_check.connect(ip_a, str(nmap(ip_a)[i])) == 0 :
                print(nmap(ip_a)[i], 'is not Telnet port')
            if telnet_check.connect(ip_a, str(nmap(ip_a)[i])) == 1 :
                print(nmap(ip_a)[i], 'is Telnet port!!')
                info_port[2] = 1
            


            
    
if __name__ == '__main__':
    main()
