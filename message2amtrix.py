import simplematrixbotlib as botlib
import bot_fwd
import auth

auth.load_dotenv()

creds = botlib.Creds(bot_fwd.HOMESERVER, bot_fwd.USERNAME, bot_fwd.PASSWORD)
bot = botlib.Bot(creds)
PREFIX = '!'

@bot.listener.on_message_event
async def echo(room, message):
    match = botlib.MessageMatch(room, message, bot, PREFIX)

    if match.is_not_from_this_bot() and match.prefix() and match.command("echo"):

        await bot.api.send_text_message(
            room.room_id, " ".join(arg for arg in match.args())
            )

bot.run()