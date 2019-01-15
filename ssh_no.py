
import subprocess


def getCallResult(cmdARGS):

  fd_popen = subprocess.Popen(cmdARGS.split(), stdout=subprocess.PIPE).stdout

  data = fd_popen.read().strip()

  fd_popen.close()

  return data


def ssh_check(host, port):
    
    results = getCallResult("ssh "+host+" -p "+port)

    #print (results)

    if 'closed' in results:
        print('###nono')
        a = 0
    if 'refused' in results:
        print('###nono')
        a = 0
    if 'password' in results:
        print('ssh!')
        a = 1
    else :
        a = 0

    return a



    




