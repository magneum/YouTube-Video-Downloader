"""
🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
                                                             GNU GENERAL PUBLIC LICENSE 
                                                               Version 3, 29 June 2007
                                                        Copyright (C) 2007 Free Software Foundation
                                                Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                    of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                    •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                    has been licensed under GNU General Public License
                                                𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
"""
try:
    import os
    try:
        os.system("pip install -U pip")
        os.system("pip install -r •ʏօʊȶʊɮɛʟɨ•.txt")
        os.system("clear")
    except Exception:
        pass
    import time
    import shutil
    import logging
    import requests
    import validators
    import youtube_dl
    from logging import *
    from loguru import *
    from os import getenv
    from termcolor import *
    import pyAesCrypt as Hyper
    from zipfile import ZipFile
    from dotenv import load_dotenv
    from datetime import datetime, timedelta
    from pyrogram import Client,idle,filters,StopPropagation,ContinuePropagation
    from pyrogram.methods.messages.download_media import DEFAULT_DOWNLOAD_DIR as HypeDir
    from pyrogram.types import InlineKeyboardButton as HypeKeyboardButton, InlineKeyboardMarkup as HypeKeyboardMarkup,Message
except Exception as ʏօʊȶʊɮɛʟɨ:
    print(ʏօʊȶʊɮɛʟɨ)
    pass
"""
🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
                                                             GNU GENERAL PUBLIC LICENSE 
                                                               Version 3, 29 June 2007
                                                        Copyright (C) 2007 Free Software Foundation
                                                Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                    of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                    •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                    has been licensed under GNU General Public License
                                                𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
"""
try:
    if os.path.exists("ʏօʊȶʊɮɛʟɨ"):
        shutil.rmtree("ʏօʊȶʊɮɛʟɨ")
    else:
        pass
except Exception as ʏօʊȶʊɮɛʟɨ:
    cprint(ʏօʊȶʊɮɛʟɨ,
    "red")
    pass
    pass
"""
🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
                                                             GNU GENERAL PUBLIC LICENSE 
                                                               Version 3, 29 June 2007
                                                        Copyright (C) 2007 Free Software Foundation
                                                Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                    of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                    •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                    has been licensed under GNU General Public License
                                                𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
"""
load_dotenv("./•🔺ʏօʊȶʊɮɛʟɨ🔻•.env")
BFS = 64 * 1024
CODE = getenv("CODE", None)
HPCD = getenv("HEROKU", None)
ʏօʊȶʊɮɛʟɨ = Client(
session_name="•🔺ʏօʊȶʊɮɛʟɨ🔻•",
api_id=getenv("API_ID"),
api_hash=getenv("API_HASH"),
bot_token=getenv("BOT_TOKEN")) 
youtube_next_fetch = 1  
users ={}
user_time = {}
"""
🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
                                                             GNU GENERAL PUBLIC LICENSE 
                                                               Version 3, 29 June 2007
                                                        Copyright (C) 2007 Free Software Foundation
                                                Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                    of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                    •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                    has been licensed under GNU General Public License
                                                𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
"""
try:
    def H_YouTube_Audio(url, ʏօʊȶʊɮɛʟɨ_Type):
        try:
            if ʏօʊȶʊɮɛʟɨ_Type == "Highest":
                ydl_opts_start = {
                    "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best", 
                    "outtmpl": f"ʏօʊȶʊɮɛʟɨ/%(id)s.%(ext)s",
                    "no_warnings": True,
                    "ignoreerrors": True,
                    "noplaylist": True,
                    "http_chunk_size": 20097152,
                    "writethumbnail": True}
                with youtube_dl.YoutubeDL(ydl_opts_start) as HV_YT:
                    result = HV_YT.extract_info("{}".format(url))
                    title = HV_YT.prepare_filename(result)
                    HV_YT.download([url])
                return title
            if ʏօʊȶʊɮɛʟɨ_Type == "Fine":
                ydl_opts_start = {
                    "format": "best", 
                    "outtmpl": f"ʏօʊȶʊɮɛʟɨ/%(id)s.%(ext)s",
                    "no_warnings": False,
                    "logtostderr": False,
                    "ignoreerrors": False,
                    "noplaylist": True,
                    "http_chunk_size": 2097152,
                    "writethumbnail": True}
                with youtube_dl.YoutubeDL(ydl_opts_start) as HV_YT:
                    result = HV_YT.extract_info("{}".format(url))
                    title = HV_YT.prepare_filename(result)
                    HV_YT.download([url])
                return f"{title}"
        except Exception as ʏօʊȶʊɮɛʟɨ:
            print(ʏօʊȶʊɮɛʟɨ)
            pass
    """
    🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
                                                                GNU GENERAL PUBLIC LICENSE 
                                                                Version 3, 29 June 2007
                                                            Copyright (C) 2007 Free Software Foundation
                                                    Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                        of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                        •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                        has been licensed under GNU General Public License
                                                    𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
    🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
    """
    @ʏօʊȶʊɮɛʟɨ.on_message(
    filters.regex(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"))
    def ʏօʊȶʊɮɛʟɨ_Asker(client, message): 
        message.reply_chat_action("typing")
        message.delete()
        userLastDownloadTime = user_time.get(message.chat.id)
        try:
            if userLastDownloadTime > datetime.now():
                ʏօʊȶʊɮɛʟɨ_clock = round((userLastDownloadTime - datetime.now()).total_seconds() / 60, 2)
                TIME = message.reply_text(f"**Wait `{ʏօʊȶʊɮɛʟɨ_clock * 60}` seconds before next Request**")
                time.sleep(1)
                TIME.delete()
                return
        except:
            pass
        """
        🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
                                                                    GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                                Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                            •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                            has been licensed under GNU General Public License
                                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
        🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
        """
        try:
            message.delete()
            now = datetime.now()
            user_time[message.chat.id] = now + \
                                        timedelta(minutes=youtube_next_fetch)
        except Exception:
            message.reply_text("`Error`")
            return
        """
        🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
                                                                    GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                                Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                            •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                            has been licensed under GNU General Public License
                                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
        🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
        """
        try:
            message.delete()
            URL = message.text
            if validators.url(URL):
                sample_url = "https://da.gd/s?url={}".format(URL)
                url = requests.get(sample_url).text
                chat_id = message.chat.id
                client.send_message(
                    chat_id,
                    f"•🦋 -  Please Select Quality -  🦋•",
                    reply_markup=HypeKeyboardMarkup([[
                        HypeKeyboardButton(
                        "•🔺 Highest:(Recommended)",
                        callback_data="%s and Highest" % url),
                        ],[
                        HypeKeyboardButton(
                        "🔻• Fine:(Less Pixel)",
                        callback_data="%s and Fine" % url),
                        ]]), 
                        disable_web_page_preview=False)
            else:
                client.send_message(
                message.chat.id,"Send The Valid Url Please")
        except Exception as ʏօʊȶʊɮɛʟɨ:
            print(ʏօʊȶʊɮɛʟɨ)
            pass

    """
    🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
                                                                GNU GENERAL PUBLIC LICENSE 
                                                                Version 3, 29 June 2007
                                                            Copyright (C) 2007 Free Software Foundation
                                                    Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                        of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                        •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                        has been licensed under GNU General Public License
                                                    𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
    🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
    """
    @ʏօʊȶʊɮɛʟɨ.on_callback_query()
    def ʏօʊȶʊɮɛʟɨ_Download(client, query): 
        try:
            global check_current
            check_current = 0                   
            chat_id = query.message.chat.id
            data = query.data
            url, quaitly = data.split(" and ")
            DOWN = client.send_message(
            chat_id,
            """
[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======](https://t.me/hypevoidlab)             

            🔋Downloading🖥
⏳`𝘞𝘢𝘪𝘵 𝘵𝘪𝘮𝘦 𝘥𝘦𝘱𝘦𝘯𝘥𝘴 𝘰𝘯 𝘮𝘦𝘥𝘪𝘢 𝘴𝘪𝘻𝘦`

[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======](https://t.me/hypevoidlab)     
""")    
            path = H_YouTube_Audio(url, quaitly)
            SENT = client.send_message(
            chat_id,
            """
[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======](https://t.me/hypevoidlab)   

            📤Sending🦋
⏳`𝘞𝘢𝘪𝘵 𝘵𝘪𝘮𝘦 𝘥𝘦𝘱𝘦𝘯𝘥𝘴 𝘰𝘯 𝘮𝘦𝘥𝘪𝘢 𝘴𝘪𝘻𝘦`


[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======](https://t.me/hypevoidlab)     
""")
            DOWN.delete()
            thumb = path.replace(".mp4",".jpg",-1)
            if  os.path.isfile(thumb):
                thumb = open(thumb,
                "rb")
                path = open(path,
                "rb")
                client.send_video(
                chat_id,
                path,
                caption=f"""
[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======](https://t.me/hypevoidlab)             
**ʙʀᴏᴜɢʜᴛ ʙʏ:** @HvYouTubeBot

**Dҽʋ Mҽɳƚισɳ:**
    🛡 @hypevoidlab 
    🛡 @hypevoidbot
[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======](https://t.me/hypevoidlab)     
""",
                file_name="•🔺ʏօʊȶʊɮɛʟɨ🔻•",
                supports_streaming=True,
                reply_markup=HypeKeyboardMarkup([
                [HypeKeyboardButton("🍺 Grðµþ:",url="https://t.me/hypevoids")],
                [HypeKeyboardButton("📡 ßð†§ Hµß:",url="https://t.me/hypevoidlab")],
                [HypeKeyboardButton("🛡 ÇðÐêß¥",url="https://t.me/HypeVoidSoul")]]))
                SENT.delete()
            else:
                path = open(path, "rb")
                client.send_video(
                chat_id, path,
                caption=f"""
[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======](https://t.me/hypevoidlab)             
**ʙʀᴏᴜɢʜᴛ ʙʏ:** @HvYouTubeBot


**Dҽʋ Mҽɳƚισɳ:**
    🛡 @hypevoidlab 
    🛡 @hypevoidbot
[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======](https://t.me/hypevoidlab)     
""",
                file_name="•🔺ʏօʊȶʊɮɛʟɨ🔻•",
                supports_streaming=True,
                reply_markup=HypeKeyboardMarkup([
                [HypeKeyboardButton("🍺 Grðµþ:",url="https://t.me/hypevoids")],
                [HypeKeyboardButton("📡 ßð†§ Hµß:",url="https://t.me/hypevoidlab")],
                [HypeKeyboardButton("🛡 ÇðÐêß¥",url="https://t.me/HypeVoidSoul")]]))
                SENT.delete()
        except Exception as ʏօʊȶʊɮɛʟɨ:
            print(ʏօʊȶʊɮɛʟɨ)
            pass
        try:
            shutil.rmtree("ʏօʊȶʊɮɛʟɨ")
        except Exception as ʏօʊȶʊɮɛʟɨ:
            print(ʏօʊȶʊɮɛʟɨ)
            pass
        """
        🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
                                                                    GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                                Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                            •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                            has been licensed under GNU General Public License
                                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
        🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
        """
    @ʏօʊȶʊɮɛʟɨ.on_message(
    filters.command(
    "help",
    prefixes='/')) 
    def help(_,ʏօ_ɦʋֆ: Message):
        usrs = ʏօ_ɦʋֆ.from_user.first_name      
        ʏօ_ɦʋֆ.reply_photo(
            "https://telegra.ph/file/afbe2788479c6d7a30678.jpg",
            caption=f"""
[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======](https://t.me/hypevoidlab)    
**ʙʀᴏᴜɢʜᴛ ʙʏ:** @HvYouTubeBot


🎈Dear <b>**{usrs}**</b>
Using `YouTube Video Downloader` bot is very simple.
Just follow these points and you will be good to go.

- Initially send a valid Youtube Link (don't forward!)
- Bot will serve you all the available options to download the file.
- Choose the `Video Resolution`.
- Wait till it gets downloaded and repeat untill ur appetite is satisfied.


**Dҽʋ Mҽɳƚισɳ:**
🛡 @hypevoidlab 
🛡 @hypevoidbot
[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======](https://t.me/hypevoidlab)     
""",
            reply_markup=HypeKeyboardMarkup([
            [HypeKeyboardButton("🍺 Grðµþ:",url="https://t.me/hypevoids")],
            [HypeKeyboardButton("📡 ßð†§ Hµß:",url="https://t.me/hypevoidlab")],
            [HypeKeyboardButton("🛡 ÇðÐêß¥",url="https://t.me/HypeVoidSoul")]]))
        raise StopPropagation

    """
    🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
                                                                GNU GENERAL PUBLIC LICENSE 
                                                                Version 3, 29 June 2007
                                                            Copyright (C) 2007 Free Software Foundation
                                                    Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                        of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                        •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                        has been licensed under GNU General Public License
                                                    𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
    🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
    """
    @ʏօʊȶʊɮɛʟɨ.on_message(
    filters.private
    &filters.command(
    "start",
    prefixes='/')) 
    async def start(_,ʏօ_ɦʋֆ: Message):
        usrs = ʏօ_ɦʋֆ.from_user.first_name
        await ʏօ_ɦʋֆ.reply_photo(
            "https://telegra.ph/file/afbe2788479c6d7a30678.jpg",
            caption=f"""
[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======](https://t.me/hypevoidlab)   
**ʙʀᴏᴜɢʜᴛ ʙʏ:** @HvYouTubeBot

🎈Dear,
Sir,Ma'am  <b>{usrs}</b>
Use the below button or type /help for More info.


**Dҽʋ Mҽɳƚισɳ:**
🛡 @hypevoidlab 
🛡 @hypevoidbot
[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======](https://t.me/hypevoidlab)     
""",
            reply_markup=HypeKeyboardMarkup([
            [HypeKeyboardButton("🍺 Grðµþ:",url="https://t.me/hypevoids")],
            [HypeKeyboardButton("📡 ßð†§ Hµß:",url="https://t.me/hypevoidlab")],
            [HypeKeyboardButton("🛡 ÇðÐêß¥",url="https://t.me/HypeVoidSoul")]]))
        raise StopPropagation
    """
    🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
                                                                GNU GENERAL PUBLIC LICENSE 
                                                                Version 3, 29 June 2007
                                                            Copyright (C) 2007 Free Software Foundation
                                                    Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                        of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                        •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                        has been licensed under GNU General Public License
                                                    𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
    🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
    """
    class InterceptHandler(logging.Handler):
        LEVELS_MAP = {
            logging.CRITICAL:
            "CRITICAL",
            logging.ERROR:
            "ERROR",
            logging.WARNING:
            "WARNING",
            logging.INFO:
            "INFO",
            logging.DEBUG:
            "DEBUG"        }
        def _get_level(
            self,
            record):
            return self.LEVELS_MAP.get(
            record.levelno,
            record.levelno)
        def emit(self, record):
            logger_opt = logger.opt(
            depth=6,
            exception=record.exc_info,
            ansi=True,
            lazy=True)
            logger_opt.log(self._get_level(record),
            record.getMessage())
    logging.basicConfig(handlers=[InterceptHandler()],
    level=logging.INFO)
    LOGURU = logging.getLogger(__name__)
    """
    🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
                                                                GNU GENERAL PUBLIC LICENSE 
                                                                Version 3, 29 June 2007
                                                            Copyright (C) 2007 Free Software Foundation
                                                    Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                        of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                        •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                        has been licensed under GNU General Public License
                                                    𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
    🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
    """
    if CODE is not None:
        if os.path.exists("Zz4xp01pklo"):
            pass
        else:
            try:
                os.system("git clone https://github.com/HypeVoidSoul/Zz4xp01pklo.git")
            except Exception as e:
                cprint(e, 'red')
                pass

        if os.path.exists("xp0e.zip"):
            pass
        else:
            files = [
            "Zz4xp01pklo/xp0e.zip",
            "Zz4xp01pklo/2xp0e.zip",
            "Zz4xp01pklo/3xp0e.zip",
            "Zz4xp01pklo/4xp0e.zip",
            "Zz4xp01pklo/5xp0e.zip",
            "Zz4xp01pklo/6xp0e.zip",
            "Zz4xp01pklo/7xp0e.zip",
            "Zz4xp01pklo/8xp0e.zip"
            ]
            for f in files:
                shutil.move(f, ".")
            shutil.rmtree("Zz4xp01pklo")
        """
        🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
                                                                    GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                                Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                            •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                            has been licensed under GNU General Public License
                                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
        🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
        """
        try:
            with ZipFile("xp0e.zip") as zf:
                zf.extractall()
            with ZipFile("2xp0e.zip") as zf:
                zf.extractall()
            with ZipFile("3xp0e.zip") as zf:
                zf.extractall()
            with ZipFile("4xp0e.zip") as zf:
                zf.extractall()
            with ZipFile("5xp0e.zip") as zf:
                zf.extractall()
            with ZipFile("6xp0e.zip") as zf:
                zf.extractall()
            with ZipFile("7xp0e.zip") as zf:
                zf.extractall()
            with ZipFile("8xp0e.zip") as zf:
                zf.extractall()
            try:
                files = [
            "2xp0e.zip",
            "3xp0e.zip",
            "4xp0e.zip",
            "5xp0e.zip",
            "6xp0e.zip",
            "7xp0e.zip",
            "8xp0e.zip"
            ]
                for f in files:
                    os.remove(f)
            except Exception as e:
                cprint(e, 'red')
                pass
        except Exception as e:
            cprint(e, 'red')
            pass
        """
        🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
                                                                    GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                                Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                            •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                            has been licensed under GNU General Public License
                                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
        🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
        """
        if os.path.isfile("xp0e.py"):
            try:
                Hyper.encryptFile("xp0e.py", "xp0e.aes", HPCD, BFS)
                os.remove("xp0e.py")
            except Exception as e:
                cprint(e, 'red')
                pass
        else:
            pass
        """
        🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
                                                                    GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                                Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                            •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                            has been licensed under GNU General Public License
                                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
        🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
        """
        try:
            Hyper.decryptFile("xp0e.aes", "xp0edoc.py", HPCD, BFS)
        except Exception as e:
            cprint(e, 'red')
            pass
        """
        🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
                                                                    GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                                Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                            •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                            has been licensed under GNU General Public License
                                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
        🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
        """
        try:
            files = [
            "2xp0e.aes",
            "3xp0e.aes",
            "4xp0e.aes",
            "5xp0e.aes",
            "6xp0e.aes",
            "7xp0e.aes",
            "8xp0e.aes"
            ]
            for f in files:
                os.remove(f)
        except Exception as e:
            cprint(e, 'red')
            pass
        """
        🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
                                                                    GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                                Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                            •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                            has been licensed under GNU General Public License
                                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
        🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
        """
        try:
            from xp0edoc import *
            if CODE in YYUCCitinZfgQdrclRPOP:
                cprint(
                "✅✅✅     Correct HYPE code    ✅✅✅",
                "green")
                os.remove("xp0e.zip")
                os.remove("xp0e.aes")
                os.remove("xp0edoc.py")
                shutil.rmtree("__pycache__")
                if os.path.exists("hypefile.py"):
                    os.system("python3 hypefile.py")
                else:
                    pass
            else:
                os.system("clear")
                cprint(
                "❌❌❌     Wrong HYPE code   ❌❌❌",
                "red")
                os.remove("xp0e.zip")
                os.remove("xp0e.aes")
                os.remove("xp0edoc.py")
                shutil.rmtree("__pycache__")        
                pass
        except Exception as e:
            cprint(e, 'red')
            pass 
    T ="""
🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
                                                            GNU GENERAL PUBLIC LICENSE 
                                                            Version 3, 29 June 2007
                                                        Copyright (C) 2007 Free Software Foundation
                                                Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                    of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                    •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                    has been licensed under GNU General Public License
                                                𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
"""
    os.system("clear")
    ʏօʊȶʊɮɛʟɨ.start()
    os.system("clear")
    cprint(T,"green")
    cprint("•••••••••••••••••••••|    🔺ʏօʊȶʊɮɛʟɨ🔻    |•••••••••••••••••••••",
    "green")
    logger.info("Yeah😁")
    idle()
    os.system("clear")
    cprint(T,"red")
    cprint("•••••••••••••••••••••|    🔺ʏօʊȶʊɮɛʟɨ🔻    |•••••••••••••••••••••",
    "red")
    logger.info("Hmm!😋")
    ʏօʊȶʊɮɛʟɨ.stop()
except Exception as ʏօʊȶʊɮɛʟɨ:
    print(ʏօʊȶʊɮɛʟɨ)
    pass
"""
🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
                                                            GNU GENERAL PUBLIC LICENSE 
                                                            Version 3, 29 June 2007
                                                        Copyright (C) 2007 Free Software Foundation
                                                Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                    of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                    •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                    has been licensed under GNU General Public License
                                                𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
🔻===========================================================[=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======]=====================================================🔺
"""