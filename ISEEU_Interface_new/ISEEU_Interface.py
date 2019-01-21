import argparse
import sys
import ISEEU_Scanner
import ISEEU_Analyst

#get args.
def Get_arg():
    # action='store_true' use when option does not wants arguments
    parser = argparse.ArgumentParser(description='Select Module to IP_Camera_Scan or Scan-Result-File Analysis.')
    parent_group = parser.add_mutually_exclusive_group()

    parent_group.add_argument('-n','--Network', action='store_true', help="Start Network Module")
    network_parse = parent_group.add_argument_group(title='Network Check Options')
    network_parse.add_argument('-s', '--SSH', type=str, metavar="IP",help="test ssh by input ip")
    network_parse.add_argument('-e','--Telnet',type=str, metavar="IP",help="test telnet by input ip")
    network_parse.add_argument('-t','--FTP',type=str, metavar="IP",help="test ftp by input ip")
    network_parse.add_argument('-p','--Packet',type=int, metavar="sniffing_time",help="Sniff Packet of input network interface")
    
    parent_group.add_argument('-f','--Firmware', action='store_true', help="Start Firmware Module")
    firmware_parse = parent_group.add_argument_group(title='Firmware Check Options')
    firmware_parse.add_argument('--HASH', type=str,metavar="PATH",help="Create Folder Hash")
    firmware_parse.add_argument('--SCAN', type=str,metavar="PATH",help="Scan Folder")
    parent_group.add_argument('-af','--Analysis_Firmware','-fa', action='store_true',help="Start Firmware_Analysis Module")
    parent_group.add_argument('-an','--Analysis_Network','-na',action='store_true',help="Start Network_Analysis Module")

    return parser.parse_args()

# Core of ISEEU_Interface.py
# Specify what needs to be done according to the options given.
def Interface_Execute(args):
    try:
        if args.Network is True:
            if args.Packet is not None:
                ISEEU_Scanner.Packet_Scan(args.Packet)
            else:
                if args.SSH is not None:
                    ISEEU_Scanner.Ssh_Scan(args.SSH)
                if args.Telnet is not None:
                    ISEEU_Scanner.Telnet_Scan(args.Telnet)
                if args.FTP is not None:
                    ISEEU_Scanner.Ftp_Scan(args.FTP)
        elif args.Firmware is True:
            if args.HASH is not None:
                ISEEU_Scanner.Hash_Create(args.HASH)
            if args.SCAN is not None:
                ISEEU_Scanner.Firmware_Scan(args.SCAN)
        elif args.Analysis_Firmware is True:
            ISEEU_Analyst.Firmware_Analysis()
        elif args.Analysis_Network is True:
            ISEEU_Analyst.Packet_Analysis()
        else:
            print("Wrong Input")
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

if __name__ == "__main__":
    args = Get_arg()
    Interface_Execute(args)
