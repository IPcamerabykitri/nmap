import pexpect

def connect(user, host, num):
    ssh_netkey = 'continue connecting'
    connStr = 'ssh '+ user + '@' + host+' -p '+num+' -o StrictHostKeyChecking=no -l'
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.EOF, ssh_netkey, \
            '[P|p]assword:'], timeout=10 )

    try :
        if ret == 0:
            #print('[-] Error connecting')
            a = 0
            return a
        if ret == 1:
            #print('[+] This is SSH Service')
            a = 1
            return a
        if ret == 2: 
            #print('[+] This is ssh service.. but error')
            a = 1
            return a
        else :
            a = 0
            return a
    except pexpect.EOF:
        print'EOF@!!!!!!'

    chlid.close()
    
    return a
