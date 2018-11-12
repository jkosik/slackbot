#!/bin/bash

pgrep -x "python3"
EXITCODE=$?
printf "Exit code=$EXITCODE \n"
if [[ $EXITCODE != 0 ]]
    then
        printf "Secbot is down. Restarting...\n"
        pkill python3; cd "{{ bots_dir }}"; python3 secbot.py &>>/var/log/secbot.log
    else
        printf "Secbot is up. OK...\n"
fi

