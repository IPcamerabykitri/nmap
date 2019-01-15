import pexpect

def ssh_cmd(user,ip,cmd,port): 
    ssh = pexpect.spawn('ssh %s@%s "%s"' % (user,ip,cmd)) 
    try: 
        i = ssh.expect(['password:', 'continue connecting (yes/no)?'],timeout=5) 
        if i == 0 : 
            ssh.sendline(passwd) 
        elif i == 1: 
            ssh.sendline('yes') 
            ssh.expect('password: ') 
            ssh.sendline(passwd) 
    except pexpect.EOF: 
        print "EOF" 
    except pexpect.TIMEOUT:
        print "TIMEOUT"
    else:
        r = ssh.read() 
        print r
    ssh.close() 
