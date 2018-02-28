#!/usr/bin/python3

import os
import time
from gtts import gTTS
from slackclient import SlackClient

SLACKTOKEN = 'CHANGEME'


sc = SlackClient(SLACKTOKEN)
if sc.rtm_connect():  # connect to a Slack RTM websocket
    while True:
        post=sc.rtm_read()  # read all data from the RTM websocket
        print(post)
        for e in post:
            if 'text' in e.keys():
                print(e['text'])        
                say=e['text']
                if 'Alert for Graylog' in say:
                    for item in say.split("\n"):
                        if '&gt;' in item:
                            print("Parsed: ", item.strip());
                            print("Stripped: ",item.strip().split(";",1)[1]);
                            say=item.strip().split(";",1)[1]
                            tts = gTTS(text=say, lang='en')
                            tts.save("say.mp3")
                            os.system("mpg321 say.mp3")
#                            os.system('say {}'.format(say)) #macos embedded tts via "$ say"
        time.sleep(1)
        
else:
    print('Connection Failed, invalid token?')


# Sample output from Slack channel
#[{'type': 'user_typing', 'channel': 'C5V1BP6QN', 'user': 'U3DS9EYPK'}]
#[{'type': 'message', 'channel': 'C5V1BP6QN', 'user': 'U3DS9EYPK', 'text': 'aa', 'ts': '1519765373.000434', 'source_team': 'T3BNAKL6Q', 'team': 'T3BNAKL6Q'}]
#[]
#[]
#[{'type': 'message', 'deleted_ts': '1519765373.000434', 'subtype': 'message_deleted', 'hidden': True, 'channel': 'C5V1BP6QN', 'previous_message': {'type': 'message', 'user': 'U3DS9EYPK', 'text': 'aa', 'ts': '1519765373.000434'}, 'event_ts': '1519765381.000316', 'ts': '1519765381.000316'}]
