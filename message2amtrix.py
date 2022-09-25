import simplematrixbotlib as botlib
import bot_fwd
import auth
import os

auth.load_dotenv()
ROOM = os.environ['ROOM']


creds = botlib.Creds(bot_fwd.HOMESERVER, bot_fwd.USERNAME, bot_fwd.PASSWORD)
bot = botlib.Bot(creds)
PREFIX = '!'

@bot.listener.on_message_event
async def bruh(room, message):
    match = botlib.MessageMatch(room, message, bot, PREFIX)

    if match.is_not_from_this_bot() and match.prefix() and match.command("bruh"):
        print(room.room_id)
        await bot.api.send_text_message(
            room.room_id, " ".join(arg for arg in match.args())
            )