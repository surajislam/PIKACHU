from pyrogram import Client, filters
import requests
from pyrogram.types import Message
from io import BytesIO
from MahakRobot import pbot as app 

# Fill these out with your credentials


@app.on_message(filters.command("pic"))
def pic_command(client, message: Message):
    # Extract the name from the command
    try:
        name = message.command[1]
    except IndexError:
        client.send_message(message.chat.id, "✦ Please provide a name after the /pic command.")
        return

    # Build the Unsplash URL with the provided name
    unsplash_url = f"https://source.unsplash.com/500x500/?{name}"

    # Send the image as a photo
    try:
        response = requests.get(unsplash_url)
        if response.status_code == 200:
            client.send_photo(message.chat.id, photo=unsplash_url, caption=f"✦ ʜᴇʀᴇ's ᴀ ᴘɪᴄᴛᴜʀᴇ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ➠ {name}.\n\n✦ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥  ๛ᴍ ᴀ ʜ ᴀ ᴋ ♡゙ " )
        else:
            client.send_message(message.chat.id, "✦ғᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ ɪᴍᴀɢᴇ.")
    except requests.RequestException as e:
        client.send_message(message.chat.id, f"✦ ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ➥ {str(e)}")