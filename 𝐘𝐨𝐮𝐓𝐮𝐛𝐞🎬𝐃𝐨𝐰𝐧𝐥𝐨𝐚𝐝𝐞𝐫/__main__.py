
"""=================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═==========================================================================
                                                    GNU GENERAL PUBLIC LICENSE 
                                                        Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        ═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═ 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
====================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═======================================================================="""
import os
import sys
import time
import shutil
import ffmpeg
import logging
import asyncio
from loguru import *
from PIL import Image
from os import getenv
from termcolor import *
import pyAesCrypt as Hyper
from zipfile import ZipFile
from dotenv import load_dotenv
from youtube_dl import YoutubeDL
from urllib.parse import urlparse
from datetime import datetime, timedelta
from pyrogram import Client, filters, StopPropagation,idle
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton,Message
"""=================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═==========================================================================
                                                    GNU GENERAL PUBLIC LICENSE 
                                                        Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        ═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═ 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
====================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═======================================================================="""
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
LOGS = logging.getLogger(__name__)
"""=================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═==========================================================================
                                                    GNU GENERAL PUBLIC LICENSE 
                                                        Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        ═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═ 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
====================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═======================================================================="""
#load_dotenv("./𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫.env")
BFS = 64 * 1024
CODE = getenv("CODE", None)
HPCD = getenv("HEROKU", None)
HEROKU = getenv("HEROKU", None)
youtube_next_fetch = 1  
users ={}
user_time = {}
"""=================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═==========================================================================
                                                    GNU GENERAL PUBLIC LICENSE 
                                                        Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        ═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═ 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
====================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═======================================================================="""
try:
    𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜 = Client(workers=12,
    api_id=getenv("API_ID"),
    api_hash=getenv("API_HASH"),
    bot_token=getenv("BOT_TOKEN"),
    session_name="デ𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫デ")
    """=================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═==========================================================================
                                                        GNU GENERAL PUBLIC LICENSE 
                                                            Version 3, 29 June 2007
                                                    Copyright (C) 2007 Free Software Foundation
                                                Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                    of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                            ═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═ 
                                                has been licensed under GNU General Public License
                                            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
    ====================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═======================================================================="""
    def boot_reshape(img):
        width, height = img.size
        length = min(width, height)
        left = (width - length) / 2
        top = (height - length) / 2
        right = (width + length) / 2
        bottom = (height + length) / 2
        return img.crop((left, top, right, bottom))
    """=================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═==========================================================================
                                                        GNU GENERAL PUBLIC LICENSE 
                                                            Version 3, 29 June 2007
                                                    Copyright (C) 2007 Free Software Foundation
                                                Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                    of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                            ═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═ 
                                                has been licensed under GNU General Public License
                                            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
    ====================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═======================================================================="""
    def YouTube_Fetched_Url(url):
        url_path = urlparse(url).path
        basename = os.path.basename(url_path)
        return basename.split(".")[-1]
    """=================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═==========================================================================
                                                        GNU GENERAL PUBLIC LICENSE 
                                                            Version 3, 29 June 2007
                                                    Copyright (C) 2007 Free Software Foundation
                                                Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                    of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                            ═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═ 
                                                has been licensed under GNU General Public License
                                            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
    ====================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═======================================================================="""
    def Shape_It_To_Square(thumbnail, output):
        nonreshpedSQ = Image.open(thumbnail)
        reshpedSQ = boot_reshape(nonreshpedSQ)
        reshpedSQ.thumbnail((320,320),Image.LANCZOS)
        reshpedSQ.save(output)
    """=================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═==========================================================================
                                                        GNU GENERAL PUBLIC LICENSE 
                                                            Version 3, 29 June 2007
                                                    Copyright (C) 2007 Free Software Foundation
                                                Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                    of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                            ═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═ 
                                                has been licensed under GNU General Public License
                                            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
    ====================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═======================================================================="""
    def Shape_It_To_Square(thumbnail, output):
        nonreshpedSQQ = Image.open(thumbnail)
        nonreshpedSQQ.save(output)
    """=================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═==========================================================================
                                                        GNU GENERAL PUBLIC LICENSE 
                                                            Version 3, 29 June 2007
                                                    Copyright (C) 2007 Free Software Foundation
                                                Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                    of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                            ═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═ 
                                                has been licensed under GNU General Public License
                                            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
    ====================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═======================================================================="""
    @𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜.on_message(
    filters.private
    & filters.command(
    "start",
    prefixes="/")) 
    async def starts(_,ut: Message):
        await ut.delete()
        await ut.reply_photo(
        "https://telegra.ph/file/afbe2788479c6d7a30678.jpg",
        caption=f"""
一═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═一
||
||
📌I Am 𝐘𝐨𝐮𝐓𝐮𝐛𝐞 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 that can take any youtube video 
link and send you its music in mere seconds.
📌Just send me the 𝐘𝐨𝐮𝐓𝐮𝐛𝐞 video link and wait.
⚠️  **ONLY VIDEO! Check below button for AUDIO**
||
||
一═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═一""",
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("〽️ 𝐆𝐫𝐨𝐮𝐩",url="https://t.me/hypevoids")],
        [InlineKeyboardButton("⚜️ 𝐂𝐡𝐚𝐧𝐧𝐞𝐥",url="https://t.me/hypevoidlab")],
        [InlineKeyboardButton("𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫",url="https://t.me/HvYouTubeBot")],
        [InlineKeyboardButton("𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫",url="https://t.me/HvYouTubeMusicBot")]]))
        return StopPropagation
    """=================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═==========================================================================
                                                        GNU GENERAL PUBLIC LICENSE 
                                                            Version 3, 29 June 2007
                                                    Copyright (C) 2007 Free Software Foundation
                                                Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                    of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                            ═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═ 
                                                has been licensed under GNU General Public License
                                            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
    ====================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═======================================================================="""
    VOIDED = YouTube_Opts = {
    'format': "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
    'outtmpl': '%(title)s - %(extractor)s-%(id)s.%(ext)s',
    "no_warnings": True,
    "ignoreerrors": True,
    'writethumbnail': True}
    HV_YouTube_Video = YoutubeDL(VOIDED)
    """=================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═==========================================================================
                                                        GNU GENERAL PUBLIC LICENSE 
                                                            Version 3, 29 June 2007
                                                    Copyright (C) 2007 Free Software Foundation
                                                Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                    of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                            ═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═ 
                                                has been licensed under GNU General Public License
                                            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
    ====================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═======================================================================="""
    @𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜.on_message(
    filters.regex(r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"))
    async def just_get_message(_,ut: Message):
        await just_get_Message(ut)   
    async def just_get_Message(ut: Message):
        ut.reply_chat_action("typing")
        ut.delete()
        userLastDownloadTime = user_time.get(ut.chat.id)
        try:
            if userLastDownloadTime > datetime.now():
                ʏօʊȶʊɮɛʟɨ_clock = round((userLastDownloadTime - datetime.now()).total_seconds() / 60, 2)
                TIME = ut.reply_text(f"**Wait `{ʏօʊȶʊɮɛʟɨ_clock * 60}` seconds before next Request**")
                time.sleep(1)
                TIME.delete()
                return
        except:
            pass

        try:
            ut.delete()
            now = datetime.now()
            user_time[ut.chat.id] = now + \
                                        timedelta(minutes=youtube_next_fetch)
        except Exception as e:
            ut.reply_text("`Error`")
            if HEROKU == "HEROKU":
                LOGS.info(str(e))
            else:
                cprint(e,"cyan")
            pass 
            return

        await ut.reply_chat_action("playing")
        await ut.delete()
        try:
            Video_Hole = HV_YouTube_Video.extract_info(ut.text, download=True)
            if Video_Hole['duration'] > 1800:
                await ut.reply_photo(
        "https://telegra.ph/file/afbe2788479c6d7a30678.jpg",
        caption=f"""
一═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═一
||
||
⚠️  **Telegram Does not allow users to download media size bigger then 2000mb!**
⚠️  **Please try less then 30min of Video...**
||
||
一═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═一""")
                return
            Master_Status_Dl = await ut.reply_text("🎬Fetching....",
            quote=True,
            disable_notification=False)
            HV_YouTube_Video.process_info(Video_Hole)
            video_file = HV_YouTube_Video.prepare_filename(Video_Hole)
            task = asyncio.create_task(video_sender(ut, Video_Hole,video_file))
            await ut.reply_chat_action("record_video")
            await Master_Status_Dl.delete()
            while not task.done():
                await asyncio.sleep(1)
                await ut.reply_chat_action("playing")
            await ut.reply_chat_action("cancel")
            if ut.chat.type == "private":
                await ut.delete()
        except Exception as e:
            await ut.reply_text(repr(e))
            if HEROKU == "HEROKU":
                LOGS.info(str(e))
            else:
                cprint(e,"cyan")
            pass 
    """=================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═==========================================================================
                                                        GNU GENERAL PUBLIC LICENSE 
                                                            Version 3, 29 June 2007
                                                    Copyright (C) 2007 Free Software Foundation
                                                Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                    of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                            ═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═ 
                                                has been licensed under GNU General Public License
                                            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
    ====================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═======================================================================="""
    async def video_sender(ut: Message, Video_Hole, video_file):
        basename = video_file.rsplit(".", 1)[-2]
        if Video_Hole['ext'] == 'webm':
            video_file_opus = basename + ".opus"
            ffmpeg.input(video_file).output(video_file_opus, codec="copy").run()
            os.remove(video_file)
            video_file = video_file_opus
        thumbnail_url = Video_Hole['thumbnail']
        if os.path.isfile(basename + ".jpg"):
            Master_Thumb = basename + ".jpg"
        else:
            Master_Thumb = basename + "." + \
                YouTube_Fetched_Url(thumbnail_url)
        resized_thumb = basename + "_reshpedSQ.jpg"
        Shape_It_To_Square(Master_Thumb, resized_thumb)
        webpage_url = Video_Hole['webpage_url']
        title = Video_Hole['title']
        duration = int(float(Video_Hole['duration']))
        performer = Video_Hole['uploader']
        if os.path.isfile(basename + ".jpg"):
            SQ_Thumb = basename + ".jpg"
        else:
            SQ_Thumb = basename + "." + \
                YouTube_Fetched_Url(thumbnail_url)
        Squared_Thumb = basename + "_nonreshpedSQQ.jpg"
        Shape_It_To_Square(SQ_Thumb, Squared_Thumb)
        void = await ut.reply_photo(
            Squared_Thumb,
            caption=f"""
        ✨🤩 𝙽𝚒𝚌𝚎 𝚌𝚑𝚘𝚒𝚌𝚎! 🤩✨ 
🛒𝚈𝚘𝚞𝚛 𝙰𝚞𝚍𝚒𝚘 𝚏𝚒𝚕𝚎 𝚠𝚒𝚕𝚕 𝚋𝚎 𝚑𝚎𝚛𝚎 𝚜𝚑𝚘𝚛𝚝𝚕𝚢
||
|   **Title:** {title}
|   **ꜱɪᴛᴇ:** [🎬𝐘𝐨𝐮𝐓𝐮𝐛𝐞](https://youtube.com)
|   **Performer:** [{performer}](https://t.me/hypevoidlab)
|   **Duration:** [{duration}s](https://t.me/hypevoidlab)
|   **Webpage:** [{webpage_url}](https://t.me/hypevoidlab)
||
一═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═一""",
            parse_mode='markdown')
        await ut.reply_video(
            video_file,
            reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("〽️ 𝐆𝐫𝐨𝐮𝐩",url="https://t.me/hypevoids")],
            [InlineKeyboardButton("⚜️ 𝐂𝐡𝐚𝐧𝐧𝐞𝐥",url="https://t.me/hypevoidlab")],
            [InlineKeyboardButton("𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫",url="https://t.me/HvYouTubeBot")],
            [InlineKeyboardButton("𝐘𝐨𝐮𝐓𝐮𝐛𝐞⭕️𝐌𝐮𝐬𝐢𝐜⭕️𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫",url="https://t.me/HvYouTubeMusicBot")]]),
            caption=f"""
一═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═一
||
|   **Title:** {title}
|   **ꜱɪᴛᴇ:** [🎬𝐘𝐨𝐮𝐓𝐮𝐛𝐞](https://youtube.com)
|   **Performer:** [{performer}](https://t.me/hypevoidlab)
|   **Duration:** [{duration}s](https://t.me/hypevoidlab)
|   **Webpage:** [{webpage_url}](https://t.me/hypevoidlab)
||
一═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═一
    """,
            thumb=resized_thumb)
        await void.delete()
        try:
            os.remove(video_file)
            os.remove(Master_Thumb)
            os.remove(resized_thumb)
            os.remove(Squared_Thumb) 
        except Exception as e:
            if HEROKU == "HEROKU":
                LOGS.info(str(e))
            else:
                cprint(e,"cyan")
            pass 
        return StopPropagation
    UTUBE = """
    =================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═==========================================================================
                                                        GNU GENERAL PUBLIC LICENSE 
                                                            Version 3, 29 June 2007
                                                    Copyright (C) 2007 Free Software Foundation
                                                Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                    of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                            ═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═ 
                                                has been licensed under GNU General Public License
                                            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
    ====================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═=======================================================================
    """
    if CODE is not None:
        if os.path.exists("Zz4xp01pklo"):
            pass
        else:
            try:
                os.system("git clone https://github.com/HypeVoidSoul/Zz4xp01pklo.git")
            except Exception as e:
                if HEROKU == "HEROKU":
                    LOGS.info(str(e))
                else:
                    cprint(e,"cyan")
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
                if HEROKU == "HEROKU":
                    LOGS.info(str(e))
                else:
                    cprint(e,"cyan")
                pass 
        except Exception as e:
            if HEROKU == "HEROKU":
                LOGS.info(str(e))
            else:
                cprint(e,"cyan")
            pass 
        """=================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═==========================================================================
                                                            GNU GENERAL PUBLIC LICENSE 
                                                                Version 3, 29 June 2007
                                                        Copyright (C) 2007 Free Software Foundation
                                                    Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                        of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                ═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═ 
                                                    has been licensed under GNU General Public License
                                                𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
        ====================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═======================================================================="""
        if os.path.isfile("xp0e.py"):
            try:
                Hyper.encryptFile("xp0e.py", "xp0e.aes", HPCD, BFS)
                os.remove("xp0e.py")
            except Exception as e:
                if HEROKU == "HEROKU":
                    LOGS.info(str(e))
                else:
                    cprint(e,"cyan")
            pass 
        else:
            pass
        """=================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═==========================================================================
                                                            GNU GENERAL PUBLIC LICENSE 
                                                                Version 3, 29 June 2007
                                                        Copyright (C) 2007 Free Software Foundation
                                                    Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                        of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                ═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═ 
                                                    has been licensed under GNU General Public License
                                                𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
        ====================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═======================================================================="""
        try:
            Hyper.decryptFile("xp0e.aes", "xp0edoc.py", HPCD, BFS)
        except Exception as e:
            if HEROKU == "HEROKU":
                LOGS.info(str(e))
            else:
                cprint(e,"cyan")
            pass 
        """=================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═==========================================================================
                                                            GNU GENERAL PUBLIC LICENSE 
                                                                Version 3, 29 June 2007
                                                        Copyright (C) 2007 Free Software Foundation
                                                    Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                        of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                ═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═ 
                                                    has been licensed under GNU General Public License
                                                𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
        ====================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═======================================================================="""
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
            if HEROKU == "HEROKU":
                LOGS.info(str(e))
            else:
                cprint(e,"cyan")
            pass 
        """=================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═==========================================================================
                                                            GNU GENERAL PUBLIC LICENSE 
                                                                Version 3, 29 June 2007
                                                        Copyright (C) 2007 Free Software Foundation
                                                    Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                        of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                ═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═ 
                                                    has been licensed under GNU General Public License
                                                𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
        ====================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═======================================================================="""
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
            if HEROKU == "HEROKU":
                LOGS.info(str(e))
            else:
                cprint(e,"cyan")
            pass 
    """=================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═==========================================================================
                                                        GNU GENERAL PUBLIC LICENSE 
                                                            Version 3, 29 June 2007
                                                    Copyright (C) 2007 Free Software Foundation
                                                Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                    of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                            ═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═ 
                                                has been licensed under GNU General Public License
                                            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
    ====================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═======================================================================="""
    𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜.start()
    os.system("clear")
    cprint(UTUBE,"green")
    cprint("🍁🎷一═デ🎬_𝐘𝐨𝐮𝐓𝐮𝐛𝐞 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫_🎬デ═一","yellow")
    cprint("ONLINE🍁🎷","yellow")
    idle()
    𝐘𝐨𝐮𝐓𝐮𝐛𝐞𝐌𝐮𝐬𝐢𝐜.stop()
    os.system("clear")
    cprint(UTUBE,"red")
    cprint("🍁⚰️一═デ🎬_𝐘𝐨𝐮𝐓𝐮𝐛𝐞 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫_🎬デ═一","cyan")
    cprint("OFFLINE ⚰️🍁","red")
except Exception as e:
    if HEROKU == "HEROKU":
        LOGS.info(str(e))
    else:
        cprint(e,"cyan")
    sys.exit(1)
"""=================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═==========================================================================
                                                    GNU GENERAL PUBLIC LICENSE 
                                                        Version 3, 29 June 2007
                                                Copyright (C) 2007 Free Software Foundation
                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                        ═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═ 
                                            has been licensed under GNU General Public License
                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
====================================================================═デ 𝐘𝐨𝐮𝐓𝐮𝐛𝐞🎬𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 デ═======================================================================="""