#!/usr/bin/python3

import shlex
import subprocess
import os
import stat
import shutil


existing=next(os.walk('../plugins'))[1]
print("Already existing dirs(names) in \"plugins\" dir: {0}\n".format(existing))

existing_path = ['../plugins/{0}'.format(i) for i in existing]
print(existing_path)

#Check sanity of dirs (max. one file permitted. Any amount of dirs allowed.)
files_all=[]
for d in existing_path: 
    contents_inside=os.listdir(path=d) #list files/dirs inside
    print("Contents inside \"plugins\" dir \"{0}\": {1}".format(d, contents_inside))
    files_only = [name for name in os.listdir(d) if os.path.isfile(os.path.join(d, name))]
    file_count = len([name for name in os.listdir(d) if os.path.isfile(os.path.join(d, name))])
    print("Files inside \"{0}\" dir: {1}".format(d, files_only))
    print("File count: {0}".format(file_count))
    for f in files_only: #create relative path for every file found, e.g. 'test4/test4_file'
        path = os.path.join(d,f)
        files_all.append(path)
    if file_count > 1: 
        print("Dir \"{0}\" has more than 1 potentially executable file - RTFM. Exiting...\n".format(d))
        exit(1)
    else:
        print("Dir \"{0}\" has 0-1 potentially executable files. OK.\n".format(d))

print("All files collected in dirs: {0}".format(files_all))        

#if file count correct, make every file executable
for e in files_all:
    st = os.stat(e)
    os.chmod(e, st.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

#print("\n++++++++ Running staging test runs ++++++++")
#for e in files_all:
#    cmd = e
#    print("\nRunning {0}".format(e))
#    try:
#        p = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#        (output, err) = p.communicate()
#        print("Output: ", output.decode('utf-8'))
#        print("Error: ", err.decode('utf-8'))
#    except Exception as e:
#        print("SecBot is not happy with your code in \"{0}\"".format(e))
#        #exit(1)
#    if err:
#        print("SecBot found error. Bad bad code in \"{0}\"".format(e))
#        exit(1)



