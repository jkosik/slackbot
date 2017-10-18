#!/usr/bin/python3

import os
import time
from slackclient import SlackClient
import json
import requests
import random
import getpass
import shlex, subprocess
import re
import sys
sys.path.insert(0, '/home/juraj/vault')
from bots import *
import pyotp


BOT_NAME = 'secbot'
BOT_ID = #CHANGEME

SLACKTOKEN = BOT_SLACKTOKEN
totp = pyotp.TOTP(OTP_SECRET) #OTP stored in vault


slack_client = SlackClient(SLACKTOKEN)

# constants
AT_BOT = "<@" + BOT_ID + ">"


def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """

    existing_commands = next(os.walk('plugins'))[1] #list of commands available
    print(existing_commands)
    for c in existing_commands:
        if command.startswith(c):
            response = ""
            args = command.split()
            args.pop(0) #remove first element (command itself) to pass only args
            args_joined = " ".join(args)
            print(args_joined)
            cdir = "plugins/{0}".format(c)
            file_to_run = [name for name in os.listdir(cdir) if os.path.isfile(os.path.join(cdir, name))] #file inside "c" dir. Presence of just one file is ensured during staging tests
            print(file_to_run)
            cmd = "./plugins/{0}/{1} {2}".format(c,file_to_run[0], args_joined)
            #cmd = "python3 ./plugins/{0}/{1} {2}".format(c,file_to_run[0], args_joined)
            #print(cmd)
            p = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out = p.communicate()[0]
            p.wait()
            #print(out)
            out_list = out.decode('utf-8').split("\n")
            #print(out_list)
            response = "*Running cmd: {}* \n".format(c)
            for record in out_list:
                response += record
                response += "\n"
            break
        else:
            response = "RTFM :)\n"
            response += "or type \n ```@secbot help```"

    slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)

#####

def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
