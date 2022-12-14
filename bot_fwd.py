import simplematrixbotlib as botlib
import os
from dotenv import load_dotenv

load_dotenv()

HOMESERVER = os.environ['HOMESERVER']
USERNAME = os.environ['BOT_USERNAME']
PASSWORD = os.environ['BOT_PASSWORD']

creds = botlib.Creds(HOMESERVER, USERNAME, PASSWORD)
bot = botlib.Bot(creds)
PREFIX = '!'

import sys
from requests_html import HTMLSession
import os
from dotenv import load_dotenv
import json
print("b")
print("ruh")
print("mo")
print("ment")
load_dotenv()

EMAIL = os.environ['EMAIL']
PASSWORD = os.environ['PASSWORD']
COOKIE = os.environ['COOKIE']
ROOM = os.environ['ROOM']

URL = 'https://www.remind.com/v2/access_tokens/confirmed_login'


async def auth():
    # This is the form data that the page sends when logging in
    login_data = {
        "user": {
            "device_address": EMAIL,
            "password": PASSWORD,
        },
        "persist": False,
    }

    with HTMLSession() as session:
        # Authenticate
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0',
            'Host': 'www.remind.com',
            'Accept': 'application/json',
            'Accept-Language': 'en-US, en; q = 0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://www.remind.com/',
            'Remind101-Client-Type': 'Web',
            'Remind101-Client-Name': 'Dashboard',
            'Remind101-Client-Segment': 'desktop_web',
            'Remind101-Client-Version': 'v8039',
            'Remind101-Timezone-Id': 'America/Los_Angeles',
            'Remind101-Timezone-Offset': '-25200',
            'Origin': 'https://www.remind.com',
            'Cookie': COOKIE,
            }
        r = session.post(URL, data=json.dumps(login_data), headers=headers)
        print(r.text)
        print(r.status_code)
        if r.status_code == 403:
            emailVerify = input("Enter email verification code: ")
            email_data = {
                "address": EMAIL,
                "code": emailVerify,
            }
            emailEndpoint = "https://www.remind.com/v2/devices/outbound_verification"
            verify = session.post(emailEndpoint, data=json.dumps(email_data), headers=headers)
            print(verify.text)
        a = session.get('https://www.remind.com/v2/chats')
        activeChats = json.loads(a.text)
        print(activeChats)
        messages_dic = []
        for thingie in activeChats['chats']:
            message = thingie['last_message']['body']
            senderUID = thingie['last_message']['sender']['uuid']
            senderDisplayName = thingie['last_message']['sender']['name']
            messages_dic.append(f'{senderDisplayName} ({senderUID}): {message}')
        return messages_dic

@bot.listener.on_message_event
async def echo(room, message):
    match = botlib.MessageMatch(room, message, bot, PREFIX)

    if match.is_not_from_this_bot() and match.prefix() and match.command("echo"):
        print(room.room_id)
        await bot.api.send_text_message(
            room.room_id, " ".join(arg for arg in match.args())
            )

@bot.listener.on_message_event
async def bridge(room, message):
    match = botlib.MessageMatch(room, message, bot, PREFIX)

    if match.is_not_from_this_bot() and match.prefix() and match.command("bridge"):
        print(room.room_id)
        await bot.api.send_text_message(
            room.room_id, " ".join(arg for arg in match.args())
            )

@bot.listener.on_message_event
async def remind_message(room, message):
    match = botlib.MessageMatch(room, message, bot, PREFIX)

    if match.is_not_from_this_bot() and match.prefix() and match.command("ask"):
            print(room.room_id)
            values_dic = await auth()
            for element in values_dic:
                await bot.api.send_text_message(
                    room.room_id, str(element))



bot.run()