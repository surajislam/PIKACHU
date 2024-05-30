import json
import requests
from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto, Message
from MahakRobot import pbot as app
from requests import get 
from MahakRobot import pbot as app
from pyrogram import filters
from pyrogram.types import InputMediaPhoto

@app.on_message(filters.command(["pinrstimg"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def pinterest(_, message):
     chat_id = message.chat.id

     try:
       query= message.text.split(None,1)[1]
     except:
         return await message.reply("**ɢɪᴠᴇ ɪᴍᴀɢᴇ ɴᴀᴍᴇ ғᴏʀ sᴇᴀʀᴄʜ 🔍**")

     images = get(f"https://aiimage.hellonepdevs.workers.dev/?prompt={query}&state=url").json()

     media_group = []
     count = 0

     msg = await message.reply(f"sᴄʀᴀᴘɪɴɢ ɪᴍᴀɢᴇs ғʀᴏᴍ ᴘɪɴᴛᴇʀᴇᴛs...")
     for url in images["images"][:6]:

          media_group.append(InputMediaPhoto(media=url))
          count += 1
          await msg.edit(f"=> ᴏᴡᴏ sᴄʀᴀᴘᴇᴅ ɪᴍᴀɢᴇs {count}")

     try:

        await app.send_media_group(
                chat_id=chat_id, 
                media=media_group,
                reply_to_message_id=message.id)
        return await msg.delete()

     except Exception as e:
           await msg.delete()
           return await message.reply(f"ᴇʀʀᴏʀ : {e}")




@app.on_message(filters.command("bingimg"))
async def bingimg_search(client: Client, message: Message):
    try:
        text = message.text.split(None, 1)[
            1
        ]  # Extract the query from command arguments
    except IndexError:
        return await message.reply_text(
            "❍ ᴘʀᴏᴠɪᴅᴇ ᴍᴇ ᴀ ǫᴜᴇʀʏ ᴛᴏ sᴇᴀʀᴄʜ!"
        )  # Return error if no query is provided

    search_message = await message.reply_text(
        "🧪"
    )  # Display searching message

    # Send request to Bing image search API
    url = "https://sugoi-api.vercel.app/bingimg?keyword=" + text
    resp = requests.get(url)
    images = json.loads(resp.text)  # Parse the response JSON into a list of image URLs

    media = []
    count = 0
    for img in images:
        if count == 7:
            break

        # Create InputMediaPhoto object for each image URL
        media.append(InputMediaPhoto(media=img))
        count += 1

    # Send the media group as a reply to the user
    await message.reply_media_group(media=media)

    # Delete the searching message and the original command message
    await search_message.delete()

__mod_name__ = "ɪᴍᴀɢᴇ"
__help__ = """
 ❍ /bingimg ➛ ɢᴇɴᴇʀᴀᴛᴇ ɪᴍᴀɢᴇ ʙʏ ɢɪᴠɪɴɢ ǫᴜᴇʀʏ.
 """