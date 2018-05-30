#!/usr/bin/python3

import sys
sys.path.insert(0, '/home/ubuntu/vault')
from bots import *
import argparse
import subprocess
import shlex

parser = argparse.ArgumentParser()
parser.add_argument("shodancmd", help="shodancmd")
args = parser.parse_args()

cmd = "shodan init {0}".format(SHODANTOKEN)
p = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
response = "*Initializing Shodan* \n"

cmd = "shodan {0}".format(args.shodancmd)
f = open('plugins/shodan/internals/shodan_out', 'w')
p = subprocess.Popen(shlex.split(cmd), stdout=f, stderr=f)
out = p.communicate()[0]

with open('plugins/shodan/internals/shodan_out') as f:
    content = f.readlines()
    response += "*Shodan result:* \n"
    for record in content:
        response += record
    print(response)

