# SecBot

## Architecture
SecBot utilizes Slack Real Time Messaging API used by Slack Bots. Slack Bot is implemented using ```slackclient``` python library => ```secbot.py```  
  
```secbot.py``` runs and watches all calls to @secbot Slack account in any Slack channel, e.g. *@secbot help*  

Commands after *@secbot* are passed to ```secbot.py``` and logic is applied afterwards in SecBot VM.  
```secbot.py``` logic is applied using *plugins* which are stored in *plugins/* directory.
  
SecBot on receiving the command scans *plugins* directory and executes desired feature.


## Plugins
Plugins are pieces of code which execute desired SecBot's feature. Plugins can be written in any language. Only requirement is prescribed structure of plugins subfolders:
* plugins/
 * feature1/
     * feature_executable
     * internals/
         * arbitrary file/dir structure
 * feature2/
     * feature_executable
 * feature3/
     * feature_executable
     * internals/
         * arbitrary file/dir structure

## Initial Deployment
SecBot lives in a standalone VM. Deployment:  
```
ansible-playbook -i inventory secbot-deploy.yml
```

## Lifecycle
New features are developed in a non-master branches. New subdirectory is created in *plugins* dir, e.g. featureN and code is put inside.  
```git push``` runs a pipeline stage which checks proper structure of feature subdirectory. If everything OK, merge request can be created.
  
Merging into *master* branch triggers another pipeline stage which does ```git pull``` on SecBot VM to adopt newly created feature directory.

## Security
Plugins can be enriched by OTP verification.  
  
To create QR code for initializing Google authenticator

```
qrencode -o- -d 300 -s 10 "otpauth://totp/secbot:juraj.kosik@abc.de?secret=xxxxx" -o secbotqr.png
display secbotqr.png
```
  
To enable OTP verification within plugin:

```
import sys
sys.path.insert(0, '/home/juraj/vault')
from bots import *
import pyotp
...
totp = pyotp.TOTP(OTP_SECRET) #OTP stored in vault
...
if totp.verify(otptoken) == True:
...
```
*In case above OTP_SECRET is defined in /home/juraj/vault/bots.py*

## Examples
* @secbot help
* @secbot shodan "search --fields ip_str,port,org,hostnames net:83.131.9.0/24"
* @secbot nova list 123456
* @secbot rce 10.12.13.14 date 444475

# Slack TTS (Text to Speech)
`slack_tts.py` utilizes "Slack Legacy token" issued for bot (part of Bots integration). Script listens to posts present in all channels where bot is invited to. Script parses outputs and plays via speakers.  

When running on MacOS, no need to import gtts library. MacOS has embedded tts via `say` binary and can be used directly
When on Linux, please use gtts library and mpg321 for playing generated mp3 files.






