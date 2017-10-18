#!/usr/bin/python3

import subprocess
import urllib.request


url = "https://packages.graylog2.org/appliances/qcow2"
target_file = "plugins/g-ver/internals/out"
grep_cmd = "plugins/g-ver/internals/grep.sh"

urllib.request.urlretrieve(url, target_file)

response = "*Last available Graylog version now:* \n"

p = subprocess.Popen(grep_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out = p.communicate()
out_clean = out[0].decode('utf-8')
response += out_clean
print(response)




