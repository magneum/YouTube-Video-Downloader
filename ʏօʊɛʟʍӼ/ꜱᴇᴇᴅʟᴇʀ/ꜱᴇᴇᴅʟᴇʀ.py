import os
from PIL import Image
from ʏօʊȶʊɮɛʟɨ import *
from ʏօʊɛʟʍӼ.ꜱʏɴᴏ import *
from ʏȶɮʟɨ import *
from ɴᴜᴋᴏʟᴀ import *
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from pyrogram import Client as ɦֆ, ContinuePropagation
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaVideo,
    InputMediaAudio,
    )


@ɦֆ.on_callback_query()
async def catch_youtube_fmtid(_,mtp):
    feeder_infos = mtp.data
    if feeder_infos.startswith("ytdata||"):
        yturl = feeder_infos.split("||")[-1]
        format_id = feeder_infos.split("||")[-2]
        media_type = feeder_infos.split("||")[-3].strip()
        if media_type == 'audio':
            buttons = InlineKeyboardMarkup([[InlineKeyboardButton(GTA,callback_data=f"{media_type}||{format_id}||{yturl}"),]])
        else:
            buttons = InlineKeyboardMarkup([[InlineKeyboardButton(GTV,callback_data=f"{media_type}||{format_id}||{yturl}")]])
        await mtp.edit_message_reply_markup(buttons)
    else:
        raise ContinuePropagation

@ɦֆ.on_callback_query()
async def catch_youtube_dldata(
    c,
    q):
    feeder_infos = q.data.strip()
    yturl = feeder_infos.split("||")[-1]
    format_id = feeder_infos.split("||")[-2]
    jpeg_fetched = DLDR + \
        "/" + str(q.message.chat.id) + ".jpg"
    if os.path.exists(jpeg_fetched):
        width = 0
        height = 0
        metadata = extractMetadata(createParser(jpeg_fetched))
        if metadata.has(
            WD):
            width = metadata.get(
            WD)
        if metadata.has(
            HD):
            height = metadata.get(
            HD)
        img = Image.open(
            jpeg_fetched)
        if feeder_infos.startswith((
            AD,)):
            img.resize((
            512,
            height))
        else:
            img.resize((
            512,
            height))
        img.save(jpeg_fetched,
            "JPEG")
    if not feeder_infos.startswith((
            VD,
            AD,)):
        raise ContinuePropagation
    filext = "%(title)s.%(ext)s"
    userdir = os.path.join(os.getcwd(), DLD, str(q.message.chat.id))
    if not os.path.isdir(userdir):
        os.makedirs(userdir)
    await q.edit_message_reply_markup(
        InlineKeyboardMarkup([[InlineKeyboardButton(A1,
        callback_data=DN)]]))
    filepath = os.path.join(
        userdir,
        filext)
    audioseeder_type = [YD,"-c",PFMG,EA,AFT,"mp3",AQT,format_id,"-o",filepath,yturl,]
    videoseeder_type = [YD,"-c",ES,"-f",f"{format_id}+bestaudio","-o",filepath,HPF,yturl,]
    if feeder_infos.startswith(
        AD):
        item_id = await audioseeder(
            audioseeder_type)
        med = InputMediaAudio(
            media=item_id,
            thumb=jpeg_fetched,
            caption=PDA,
            title=os.path.basename(item_id)
        )
    if feeder_infos.startswith(
        VD):
        item_id = await videoseeder(
            videoseeder_type)
        med = InputMediaVideo(
            media=item_id,
            width=width,
            height=height,
            thumb=jpeg_fetched,
            caption=PDV,
            supports_streaming=True
        )
    loop = asyncio.get_event_loop()
    if med:
        loop.create_task(send_file(c,q,med,item_id))
    else:
        print(PMI)
