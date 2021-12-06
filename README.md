# RIG MONITOR

I builded my first GPU Mining Rig to mine Ethereum, and I found some troubles in the way. My rig was in my home network, and I wanted to monitor it, but I was away from home. So, I made this Telegram bot to get new asbout my rig and query health, hashrate, temperature,etc , and take action in case of some failure, restarting the miner software, o modifing some settings and parameters.

At the moment I wrote this project, I was using T-Rex miner and Flexpool, and their respective APIs. More mining software and pools will be added in the future.

## Table of content
1. [Requirements](#Requirements)
2. [Installing](#Instaling)
3. [Instaling via Docker](#Intaling2)
4. [Config](#Config)
5. [Usage](#Usage)

## Requirements

## Installing

### Using command line
```
# Create a virtual environment. I've used virtualenv
virtualenv develop

source develop/bin/activate

# Install required libaries

pip install -r requirements.txt

# NOTE: If you have trouble with bottle, please try:
pip install -U bootle

#Install ngrok

sudo snap install ngrok
# Check oficial website for more information: https://ngrok.com/
```

## Installing via Docker

## Config

## Usage

