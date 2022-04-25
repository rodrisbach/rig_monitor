# RIG MONITOR

Monitor your Mining Rigs, receive alerts and Telegram messages.

## Table of content
1. [Requirements](#Requirements)
2. [Installing](#Instaling)
3. [Config](#Config)
4. [Usage](#Usage)

## Requirements

## Installing

### Install ngrok
```bash
sudo snap install ngrok
#(Check oficial website for more information: https://ngrok.com/)
```

### Run ngrox

Ngrok will expose the web server running the bot to internet. If you have a paid plan, you can run Ngrok with a subdomain, getting a stable URL. Instead, if you are using a free plan, the public URL will change every time you start a tunnel. If you run "ngrok http 8080", then you stop the process, and run it agan, you could see how the public URL will change.
```bash
ngrok http 8080
#If port 8080 is already used, you can change it in config/config.json.
```
### Set up Webhook

Execute the following action:
```bash
curl https://api.telegram.org/bot<your_token>/setWebHook?url=https://<your_ngrok_url.ngrok.io>/
```

### Using command line
```bash
# Create a virtual environment. I've used virtualenv

virtualenv develop
source develop/bin/activate

# Install required libaries

pip install -r requirements.txt
# NOTE: If you have trouble with bottle, please try:
pip install -U bootle

```

###  Docker

## Config

## Usage
