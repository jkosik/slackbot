#!/bin/bash

cd /data/bots/deploy
ansible-playbook -i inventory secbot-update.yml


