from pyrogram import Client, filters
from MahakRobot import pbot as app 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

EVAA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/mahakxbot?startgroup=true"),
    ],
]

@app.on_message(filters.command("weather"))
def weather(client, message):
    try:
        # Get the location from user message
        user_input = message.command[1]
        location = user_input.strip()
        weather_url = f"https://wttr.in/{location}.png"

        # Reply with the weather information as a photo
        message.reply_photo(photo=weather_url, caption="✦ ʜᴇʀᴇ's ᴛʜᴇ ᴡᴇᴀᴛʜᴇʀ ғᴏʀ ʏᴏᴜʀ ʟᴏᴄᴀᴛɪᴏɴ.\n\n๏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➠ ๛ᴍ ᴀ ʜ ᴀ ᴋ ♡゙", reply_markup=InlineKeyboardMarkup(EVAA),)
    except IndexError:
        # User didn't provide a location
        message.reply_text("✦ Please provide a location. ♥︎ Use /weather `ᴄɪᴛʏ ɴᴀᴍᴇ`")

__help__ = """
 ❍ ɪ ᴄᴀɴ ғɪɴᴅ ᴡᴇᴀᴛʜᴇʀ ᴏғ ᴀʟʟ ᴄɪᴛɪᴇs

 ❍ /weather <ᴄɪᴛʏ>* ➛* ᴀᴅᴠᴀɴᴄᴇᴅ ᴡᴇᴀᴛʜᴇʀ ᴍᴏᴅᴜʟᴇ, ᴜsᴀɢᴇ sᴀᴍᴇ ᴀs /ᴡᴇᴀᴛʜᴇʀ
 
 ❍ /weather ᴍᴏᴏɴ * ➛* ɢᴇᴛ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛᴜs ᴏғ ᴍᴏᴏɴ
"""

__mod_name__ = "ᴡᴇᴀᴛʜᴇʀ"
