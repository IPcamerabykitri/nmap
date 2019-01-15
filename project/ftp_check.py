import pexpect

def connect(host, num):
    
    connStr = 'ftp '+host+' '+num
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.EOF, 'Name .*:', \
            '[P|p]assword:',pexpect.TIMEOUT], timeout=10 )

    try :
        if ret == 0:
            #print('[-] Error connecting')
            a = 0
            return a
        if ret == 1:
            #print('[+] This is FTP Service')
            a = 1
            return a
        if ret == 2: 
            #print('[+] This is FTP service.. ')
            a = 1
            return a
        else :
            a = 0
            return a
    except pexpect.EOF:
        print'EOF@!!!!!!'

    chlid.close()
    
    return a
