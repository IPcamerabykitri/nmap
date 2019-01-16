import pexpect

def connect(host, num):
    ssh_netkey = 'continue connecting'
    connStr = 'ssh '+ host+' -p '+num
    child = pexpect.spawn(connStr)
    ret = child.expect(['continue connecting', pexpect.TIMEOUT, pexpect.EOF, \
            '[P|p]assword:'], timeout=10 )

    try :
        if ret == 0 :
            #print('[+] This is SSH Service')
            a = 1

        if ret == 1 :
            #print('[-] Error connecting')
            a = 0

        if ret == 2 :
            #print('[-] EOF Error ')
            a = 0
              
        if ret == 3: 
            #print('[+] This is ssh service.. but error')
            a = 1

    except pexpect.EOF:
        print'EOF@!!!!!!'


    child.close()


    return a
