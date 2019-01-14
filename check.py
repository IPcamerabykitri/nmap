
import os
#import argparser
#import net

def ssh_chk(ip, num):
    ##'ip' is IP address 
    ##'num' is port number
    #for a in ip,num:    
    #    command = "ssh "+ip+" -p "+num
    #    process = os.popen(command)
    #    results = str(process.read())
    #    r = result.split()
    #    if 'continue connecting' in r :
    #        print(num,'port is SSH service')
    #    else :
    #        print(num,'port is NOT SSH service')
    command = "ssh "+ip+" -p "+num
    process = os.popen(command)
    results = str(process.read())

    





    #print(results)


        


#def main():
    #parser.argparse.ArgumentParser()
    #parser.add_argument("x", required=True)
    #args = parser.parse_args()
    
    #if args.x:
    #    print("turn on")


    #prac.ip_a is parsed IP Address 
    #print(prac.ip_a)
    
    

#if __name__ == '__main__':

 #   main()


