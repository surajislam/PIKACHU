import os
import glob
from bing_image_downloader import downloader
from telethon import events
from telethon.tl import functions, types
from MahakRobot import telethn
from MahakRobot.events import register

async def is_register_admin(chat, user):
    if isinstance(chat, (types.InputPeerChannel, types.InputChannel)):
        participant = (await telethn(functions.channels.GetParticipantRequest(chat, user))).participant
        return isinstance(participant, (types.ChannelParticipantAdmin, types.ChannelParticipantCreator))
    elif isinstance(chat, types.InputPeerChat):
        ui = await telethn.get_peer_id(user)
        ps = (await telethn(functions.messages.GetFullChatRequest(chat.chat_id))).full_chat.participants.participants
        participant = next((p for p in ps if p.user_id == ui), None)
        return isinstance(participant, (types.ChatParticipantAdmin, types.ChatParticipantCreator))
    else:
        return None

@register(pattern="^/pimg (.*)")
async def img_sampler(event):
    if event.fwd_from:
        return
    if event.is_group:
        if not (await is_register_admin(event.input_chat, event.message.sender_id)):
            await event.reply("♥︎ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ, ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜsᴇ ᴛʜɪs ᴄᴍᴅ,, ʙᴜᴛ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ɪɴ ᴍʏ ᴘᴍ.")
            return
    query = event.pattern_match.group(1)
    downloader.download(query, limit=5, output_dir='store', adult_filter_off=False, force_replace=False, timeout=60)
    download_path = os.path.join('store', query)
    os.chdir(download_path)
    types = ('*.png', '*.jpeg', '*.jpg')
    filesgrabbed = []
    for file_type in types:
        filesgrabbed.extend(glob.glob(file_type))
    
    # Send emoji message before images
    await event.reply("Here are the images you requested! 💕")

    # Send images
    await event.client.send_file(event.chat_id, filesgrabbed, reply_to=event.id)
    
    # Delete images after sending
    for file in filesgrabbed:
        os.remove(file)
    os.chdir('../../')