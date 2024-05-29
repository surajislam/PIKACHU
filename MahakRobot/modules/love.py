from pyrogram import Client, filters
import random
from MahakRobot import pbot as app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

        
def get_random_message(love_percentage):
    if love_percentage <= 30:
        return random.choice([
            "❅ ʟᴏᴠᴇ ɪs ɪɴ ᴛʜᴇ ᴀɪʀ ʙᴜᴛ ɴᴇᴇᴅs ᴀ ʟɪᴛᴛʟᴇ sᴘᴀʀᴋ.",
            "❅ ᴀ ɢᴏᴏᴅ sᴛᴀʀᴛ ʙᴜᴛ ᴛʜᴇʀᴇ's ʀᴏᴏᴍ ᴛᴏ ɢʀᴏᴡ.",
            "❅ ɪᴛ's ᴊᴜsᴛ ᴛʜᴇ ʙᴇɢɪɴɴɪɴɢ ᴏғ sᴏᴍᴇᴛʜɪɴɢ ʙᴇᴀᴜᴛɪғᴜʟ."
        ])
    elif love_percentage <= 70:
        return random.choice([
            "❅ ᴀ sᴛʀᴏɴɢ ᴄᴏɴɴᴇᴄᴛɪᴏɴ ɪs ᴛʜᴇʀᴇ. ᴋᴇᴇᴘ ɴᴜʀᴛᴜʀɪɴɢ ɪᴛ.",
            "❅ ʏᴏᴜ'ʜᴠ ɢᴏᴛ ᴀ ɢᴏᴏᴅ ᴄʜᴀɴᴄᴇ. ᴡᴏʀᴋ ᴏɴ ɪᴛ.",
            "❅ ʟᴏᴠᴇ ɪs ʙʟᴏssᴏᴍɪɴɢ, ᴋᴇᴇᴘ ɢᴏɪɴɢ."
        ])
    else:
        return random.choice([
            "❅ ᴡᴏᴡ ! ɪᴛ's ᴀ ᴍᴀᴛᴄʜ ᴍᴀᴅᴇ ɪɴ ʜᴇᴀᴠᴇɴ!",
            "❅ ᴘᴇʀғᴇᴄᴛ ᴍᴀᴛᴄʜ ! ᴄʜᴇʀɪsʜ ᴛʜɪs ʙᴏɴᴅ.",
            "❅ ᴅᴇsᴛɪɴᴇᴅ ᴛᴏ ʙᴇ ᴛᴏɢᴇᴛʜᴇʀ. ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴs!"
        ])

EVAA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/Mahakxbot?startgroup=true"),
    ],
]

@app.on_message(filters.command("love", prefixes="/"))
def love_command(client, message):
    command, *args = message.text.split(" ")
    if len(args) >= 2:
        name1 = args[0].strip()
        name2 = args[1].strip()
        
        love_percentage = random.randint(10, 100)
        love_message = get_random_message(love_percentage)

        response = f"❅ ʜᴇʀᴇ ɪs ʏᴏᴜʀ ʟᴏᴠᴇ ᴘᴇʀᴄᴇɴᴛᴀɢᴇ ⏤‌★ \n\n❅ {name1} 💞 + {name2} 💞 = {love_percentage}%\n\n{love_message}"
        #client.send_message(message.chat.id, response, reply_markup=InlineKeyboardMarkup(EVAA),)
    else:
        response = "✦ ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ᴛᴡᴏ ɴᴀᴍᴇs ᴀғᴛᴇʀ /love ᴄᴏᴍᴍᴀɴᴅ."
    client.send_message(message.chat.id, response, reply_markup=InlineKeyboardMarkup(EVAA),)

__mod_name__ = "ʟᴏᴠᴇ"

__help__ = f"""
❍ ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ᴛᴡᴏ ɴᴀᴍᴇs ᴀғᴛᴇʀ /love ᴄᴏᴍᴍᴀɴᴅ."""