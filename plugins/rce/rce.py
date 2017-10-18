#!/usr/bin/python3

import sys
sys.path.insert(0, '/home/juraj/vault')
from bots import *
import argparse
import subprocess
import shlex
import pyotp

totp = pyotp.TOTP(OTP_SECRET) #OTP stored in vault

parser = argparse.ArgumentParser()
parser.add_argument("target", help="Target VM for running the command")
parser.add_argument("rcecmd", help="Command to run on the target")
parser.add_argument("otp", help="OTP token")
args = parser.parse_args()

resolved = args.target

response = ""
if totp.verify(args.otp) == True:
    response = "Token is correct.\n"

    if args.target.startswith("<"): 
        resolved = args.target.split("|")[1].split(">")[0]
    cmd = "ssh -i /home/juraj/vault/sc-vm-juraj -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null ubuntu@{0} {1}".format(resolved, args.rcecmd)
    p = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out,err = p.communicate()
    out_list = out.decode('utf-8').split("\n")
    err_list = err.decode('utf-8').split("\n")
    all_list = err_list + out_list
    response = "*ubuntu@{0}:~$ {1}* \n".format(args.target, args.rcecmd)
    for record in all_list:
    #for record in out_list:
        response += record
        response += "\n"
    print(response)
else:
    response = "Invalid token\n"
    print(response)
#    exit(1)





