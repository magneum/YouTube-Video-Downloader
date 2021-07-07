import os
import wget
from ʏȶɮʟɨ import *
from ɴᴜᴋᴏʟᴀ import *
from PIL import Image
from ʏօʊȶʊɮɛʟɨ import *
from pyrogram.types import InlineKeyboardMarkup, Message
from pyrogram import Client, filters
from datetime import datetime, timedelta

@Client.on_message(
filters.regex(YYEX))
async def ytdl(_,ɦʋֆ: Message):
    userLastDownloadTime = user_time.get(ɦʋֆ.chat.id)
    try:
        if userLastDownloadTime > datetime.now():
            HTS = await ɦʋֆ.reply_text(WTIF)
            await asyncio.sleep(3)
            await ɦʋֆ.delete()
            await HTS.delete()
            return
    except:
        pass
    url = ɦʋֆ.text.strip()
    await ɦʋֆ.reply_chat_action(CRAV)
    title, fetchedimage, formats = ytget_lib(url)
    user_time[ɦʋֆ.chat.id] = datetime.now() + \
    timedelta(minutes=0)
    pod = InlineKeyboardMarkup(list(resmaker(formats)))
    try:
        img = wget.download(fetchedimage)
        im = Image.open(img).convert("RGB")
        hostsend = os.path.join(os.getcwd(), DLD, str(ɦʋֆ.chat.id))
        if not os.path.isdir(hostsend):
            os.makedirs(hostsend)
        urljpegclone = f"{hostsend}.jpg"
        im.save(
            urljpegclone,
            "jpeg")
        await ɦʋֆ.reply_photo(urljpegclone, caption=title, reply_markup=pod)
    except Exception as e:
        print(e)
        try:
            fetchedimage = youliurl
            await ɦʋֆ.reply_photo(
                fetchedimage,
                caption=title,
                reply_markup=pod)
        except Exception as e:
            await ɦʋֆ.reply_text(
            f"<code>{e}</code> #Error")
