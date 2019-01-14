import os
import argparse
import re
#import check

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
    
    if args.ip:
        #SUCCESS##print("turn on")
        print(nmap(ip_a))
        #check.chk(ip_a)
    

if __name__ == '__main__':
    main()


