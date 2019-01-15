import pexpect

#PROMPT = ['#', '>>> ', '> ', '\$']

#def send_command(child, cmd):
#    child.sendline(cmd)
#    child.expect(PROMPT)
#    #print(child.before)

def connect(user, host, num):
    ssh_netkey = 'continue connecting'
    connStr = 'ssh '+ user + '@' + host+' -p '+num
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.TIMEOUT, ssh_netkey, \
            '[P|p]assword:'], timeout=5 )

    try :

        if ret == 0:
            print('[-] Error connecting')
            a = 0
            return a
        if ret == 1:
            print('[+] This is SSH Service')
            a = 1
            return a
        if ret == 2: 
            print('[+] This is ssh service.. but error')
            a = 1
            return a
        else :
            a = 0
            return a
    except pexpect.EOF:
        print'EOF@!!!!!!'

    chlid.close()
    


    #child.sendline(password)
    #child.expect(PROMPT)
    #print('ret: ',ret)
    #print('child: ',child)
    return a

