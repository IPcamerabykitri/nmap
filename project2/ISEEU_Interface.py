import os
import argparse
import sys
import ISEEU_Scanner
import ISEEU_Analyst

#get args.
def Get_arg():
    parser = argparse.ArgumentParser(description='This code is written for practice about argparse')
    parser.add_argument('', type=float,
                        metavar='First_number',
                        help='What is the first number?')
    parser.add_argument('Y', type=float,
                        metavar='Second_number',
                        help='What is the second number?')
    parser.add_argument('--op', type=str, default='add',
                        choices=['add', 'sub', 'mul', 'div'],
                        help='What operation?')
    args = parser.parse_args()

#Interface
def Interface_Execute():
    try:
        print("Interface_Execute")
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
