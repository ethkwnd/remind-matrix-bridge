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

@bot.listener.on_message_event
async def echo(room, message):
    match = botlib.MessageMatch(room, message, bot, PREFIX)

    if match.is_not_from_this_bot() and match.prefix() and match.command("echo"):

        await bot.api.send_text_message(
            room.room_id, " ".join(arg for arg in match.args())
            )

@bot.listener.on_message_event
async def bridge(room, message):
    match = botlib.MessageMatch(room, message, bot, PREFIX)

    if match.is_not_from_this_bot() and match.prefix() and match.command("bridge"):

        await bot.api.send_text_message(
            room.room_id, " ".join(arg for arg in match.args())
            )

bot.run()