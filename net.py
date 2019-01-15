import os
import argparse
import re
import ssh_no

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
        #print(group)
        #Printed Only Number using re
        if group[1] == 'open':
            i = int(re.findall('\d+', group[0])[0])
            num.append(i)
        ####'i' is Open Port #### print(i)
        #um.append(i)

    return num


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--ip", help="python prac.py -i <target IP>", required=True)
    args = parser.parse_args()
    ip_a = args.ip

    #open port list = port
    #print(type(nmap(ip_a))) list

    #[ftp,ssh,telnet,http] = info_port
    info_port = [0,0,0,0] 

    #INPUT SUCCESS#
    if args.ip:
        #PRINT OPEN PORT#
        print(nmap(ip_a))
        #print(type(nmap(ip_a)[0]))      
        
        #print(ssh_check.connect('root', ip_a, str(nmap(ip_a)[0])))

        #CHECK SSH PORT#
        for i in range(0,len(nmap(ip_a))):
            if ssh_no.ssh_check(ip_a, str(nmap(ip_a)[i])) == 0 :
                print(nmap(ip_a)[i],'is not ssh port')
                info_port[1] = 0
            if ssh_no.ssh_check(ip_a, str(nmap(ip_a)[i])) == 1 :
                print(nmap(ip_a)[i],'is ssh port!!')
                info_port[1] = 1

            print(info_port)
            
        #    a = ssh_test.check(ip_a, str(nmap(ip_a)[i]))
        #    print(type(a))
        #    if a == 0:
        #        print(str(nmap(ip_a)[i]),'is NOT SSH port')
            
        #    if a == 1:
        #        print(nmap(ip_a)[i],'is SSH port')
        #        info_port[1] =1

    
if __name__ == '__main__':
    main()
