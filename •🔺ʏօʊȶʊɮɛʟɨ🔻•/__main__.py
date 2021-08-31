from __future__ import unicode_literals
"""🔻==================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•============================================================🔺
                                                             GNU GENERAL PUBLIC LICENSE 
                                                               Version 3, 29 June 2007
                                                        Copyright (C) 2007 Free Software Foundation
                                                Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                    of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                    •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                    has been licensed under GNU General Public License
                                                𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
🔺====================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•=============================================================🔻"""
# https://youtu.be/j9__UCv_VuY
try:
    import os
    import sys
    import wget
    import shutil
    import logging
    import asyncio
    import youtube_dl
    import os as hype
    from loguru import *
    from PIL import Image
    from os import getenv
    from PIL import Image
    from termcolor import *
    from sys import platform
    import pyAesCrypt as Hyper
    from zipfile import ZipFile
    Tʊɮɛ = youtube_dl.YoutubeDL()
    from dotenv import load_dotenv
    from pyrogram.types import Message
    from hachoir.parser import createParser
    from datetime import datetime, timedelta
    from hachoir.metadata import extractMetadata
    from pyrogram import Client,idle,filters,StopPropagation,ContinuePropagation
    from pyrogram.methods.messages.download_media import DEFAULT_DOWNLOAD_DIR as HypeDir
    from pyrogram.types import InlineKeyboardButton as HypeKeyboardButton,InlineKeyboardMarkup as HypeKeyboardMarkup,InputMediaVideo,InputMediaAudio
    """🔻==================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•============================================================🔺
                                                                GNU GENERAL PUBLIC LICENSE 
                                                                Version 3, 29 June 2007
                                                            Copyright (C) 2007 Free Software Foundation
                                                    Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                        of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                        •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                        has been licensed under GNU General Public License
                                                    𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
    🔺====================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•=============================================================🔻"""
    SHUTPY = {}
    BFS = 64 * 1024
    resolutiontree = []
    load_dotenv("./.env")
    CODE = getenv("CODE", None)
    HPCD = getenv("HEROKU", None)
    YTGENX = r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"
    """🔻==================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•============================================================🔺
                                                                GNU GENERAL PUBLIC LICENSE 
                                                                Version 3, 29 June 2007
                                                            Copyright (C) 2007 Free Software Foundation
                                                    Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                        of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                        •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                        has been licensed under GNU General Public License
                                                    𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
    🔺====================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•=============================================================🔻"""
    if CODE is not None:
        try:
            ʏօʊȶʊɮɛʟɨ = Client(
                session_name="ʏօ_ɦʋֆ",
                bot_token=getenv("TOKEN"),
                api_id=int(getenv("API_ID")),
                api_hash=getenv("API_HASH"),
                workers=200
                )
        except Exception as ʏօʊȶʊɮɛʟɨ:
            print(ʏօʊȶʊɮɛʟɨ)
        """🔻==================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•============================================================🔺
                                                                    GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                                Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                            •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                            has been licensed under GNU General Public License
                                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
        🔺====================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•=============================================================🔻"""
        try:
            def DLYT(
                url,
                fmid,
                custom_progress):
                ydl_opts = {
                    'format': f"{fmid}+bestaudio",
                    "outtmpl": "test+.%(ext)s",
                    'noplaylist': True,
                    'progress_hooks': [custom_progress],
                }
                with youtube_dl.YoutubeDL(ydl_opts) as Tʊɮɛ:
                    Tʊɮɛ.download([url])
        except Exception as ʏօʊȶʊɮɛʟɨ:
            print(ʏօʊȶʊɮɛʟɨ)
        """🔻==================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•============================================================🔺
                                                                    GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                                Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                            •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                            has been licensed under GNU General Public License
                                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
        🔺====================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•=============================================================🔻"""
        try:
            def GOT_MAPPED(fetchedfiles):
                resolution = fetchedfiles['format']
                if "audio" in resolution:
                    return [HypeKeyboardButton(f"🎧{resolution}{HYPE_HUMANIZER(fetchedfiles['filesize'])}",callback_data=f"ytdata||audio||{fetchedfiles['format_id']}||{fetchedfiles['yturl']}")]
                else:
                    return [HypeKeyboardButton(f"🎬{resolution}{HYPE_HUMANIZER(fetchedfiles['filesize'])}",callback_data=f"ytdata||video||{fetchedfiles['format_id']}||{fetchedfiles['yturl']}")]
        except Exception as ʏօʊȶʊɮɛʟɨ:
            print(ʏօʊȶʊɮɛʟɨ)
        """🔻==================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•============================================================🔺
                                                                    GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                                Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                            •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                            has been licensed under GNU General Public License
                                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
        🔺====================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•=============================================================🔻"""
        try:
            def RESOLUTION_MAKER(resolutiontree):
                return map(GOT_MAPPED, resolutiontree)
        except Exception as ʏօʊȶʊɮɛʟɨ:
            print(ʏօʊȶʊɮɛʟɨ)
        """🔻==================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•============================================================🔺
                                                                    GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                                Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                            •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                            has been licensed under GNU General Public License
                                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
        🔺====================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•=============================================================🔻"""
        try:
            async def VIDEO_SEEDER(command_to_exec):
                process = await asyncio.create_subprocess_exec(
                    *command_to_exec,
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE, )
                stdout, stderr = await process.communicate()
                e_response = stderr.decode().strip()
                t_response = stdout.decode().strip()
                print(e_response)
                filename = t_response.split("FetchedFiles")[-1].split('"')[1]
                return filename
        except Exception as ʏօʊȶʊɮɛʟɨ:
            print(ʏօʊȶʊɮɛʟɨ)
        """🔻==================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•============================================================🔺
                                                                    GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                                Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                            •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                            has been licensed under GNU General Public License
                                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
        🔺====================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•=============================================================🔻"""
        try: 
            async def AUDIO_SEEDER(command_to_exec):
                process = await asyncio.create_subprocess_exec(
                    *command_to_exec,
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE, )
                stdout, stderr = await process.communicate()
                e_response = stderr.decode().strip()
                t_response = stdout.decode().strip()
                print("Download error:",
                e_response)
                return t_response.split("Destination")[-1].split("Deleting")[0].split(":")[-1].strip()
        except Exception as ʏօʊȶʊɮɛʟɨ:
            print(ʏօʊȶʊɮɛʟɨ)
        """🔻==================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•============================================================🔺
                                                                    GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                                Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                            •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                            has been licensed under GNU General Public License
                                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
        🔺====================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•=============================================================🔻"""
        try:
            def YTGET_LIB(yturl):
                with Tʊɮɛ:
                    r = Tʊɮɛ.extract_info(
                    yturl,
                    download=True)
                    for format in r['formats']:
                        if not "dash" in str(format['format']).lower():
                            resolutiontree.append(
                            {
                                "format": format['format'],
                                "filesize": format['filesize'],
                                "format_id": format['format_id'],
                                "yturl": yturl
                                }
                            )
                    return r['title'], r['thumbnail'], resolutiontree
        except Exception as ʏօʊȶʊɮɛʟɨ:
            print(ʏօʊȶʊɮɛʟɨ)
        """🔻==================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•============================================================🔺
                                                                    GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                                Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                            •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                            has been licensed under GNU General Public License
                                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
        🔺====================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•=============================================================🔻"""
        try:
            def HYPE_HUMANIZER(amount,last='B'):
                if amount is None:
                    amount = 0
                else:
                    amount = int(amount)
                for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
                    if abs(amount) < 1024.0:
                        return "%3.1f%s%s" % (
                            amount,
                            unit,
                            last)
                    amount /= 1024.0
                return "%.1f%s%s" % (
                    amount,
                    'Yi',
                    last)
        except Exception as ʏօʊȶʊɮɛʟɨ:
            print(ʏօʊȶʊɮɛʟɨ)
        """🔻==================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•============================================================🔺
                                                                    GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                                Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                            •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                            has been licensed under GNU General Public License
                                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
        🔺====================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•=============================================================🔻"""
        try:
            @ʏօʊȶʊɮɛʟɨ.on_message(
            filters.command(
            "help",
            prefixes='/')) 
            async def help(_,ʏօ_ɦʋֆ: Message):
                usrs = ʏօ_ɦʋֆ.from_user.first_name      
                await ʏօ_ɦʋֆ.reply_photo(
                    "https://telegra.ph/file/afbe2788479c6d7a30678.jpg",
                    caption=f"""
=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======
        🎈Dear <b>**{usrs}**</b>

        Using `YouTube Audio/Video Downloader` bot is very simple.
        Just follow these points and you will be good to go.

        - Initially send a valid Youtube Link (don't forward!)
        - Bot will serve you all the available options to download the file.
        - Choose the `Audio/Video and The Resolution`.
        - Wait till it gets downloaded and repeat untill ur appetite is satisfied.


    Dҽʋ Mҽɳƚισɳ:
        🛡 @hypevoidlab 
        🛡 @hypevoidbot
=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======
        """)
                raise StopPropagation
        except Exception as ʏօʊȶʊɮɛʟɨ:
            print(ʏօʊȶʊɮɛʟɨ)
        """🔻==================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•============================================================🔺
                                                                    GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                                Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                            •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                            has been licensed under GNU General Public License
                                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
        🔺====================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•=============================================================🔻"""
        try:
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
=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======

        🎈Dear,
        Sir,Ma'am  <b>{usrs}</b>
        Use the below button or type /help for More info.

    Dҽʋ Mҽɳƚισɳ:
        🛡 @hypevoidlab 
        🛡 @hypevoidbot
=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======
        """,
                    reply_markup=HypeKeyboardMarkup([
                    [HypeKeyboardButton("🍺 Grðµþ:",url="https://t.me/hypevoids")],
                    [HypeKeyboardButton("📡 ßð†§ Hµß:",url="https://t.me/hypevoidlab")],
                    [HypeKeyboardButton("🛡 ÇðÐêß¥",url="https://t.me/HypeVoidSoul")]]))
                raise StopPropagation
        except Exception as ʏօʊȶʊɮɛʟɨ:
            print(ʏօʊȶʊɮɛʟɨ)
        """🔻==================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•============================================================🔺
                                                                    GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                                Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                            •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                            has been licensed under GNU General Public License
                                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
        🔺====================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•=============================================================🔻"""
        try:
            @ʏօʊȶʊɮɛʟɨ.on_callback_query()
            async def catch_youtube_fmtid(_,mtp):
                feeder_infos = mtp.data
                if feeder_infos.startswith("ytdata||"):
                    yturl = feeder_infos.split("||")[-1]
                    format_id = feeder_infos.split("||")[-2]
                    media_type = feeder_infos.split("||")[-3].strip()   
                    if media_type == 'audio':
                        buttons = HypeKeyboardMarkup([[HypeKeyboardButton("🎤 𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙",callback_data=f"{media_type}||{format_id}||{yturl}"),]])
                    else:
                        buttons = HypeKeyboardMarkup([[HypeKeyboardButton("📺 𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙",callback_data=f"{media_type}||{format_id}||{yturl}")]])
                    await mtp.edit_message_reply_markup(buttons)


                else:
                    raise ContinuePropagation
        except Exception as ʏօʊȶʊɮɛʟɨ:
            print(ʏօʊȶʊɮɛʟɨ)
        """🔻==================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•============================================================🔺
                                                                    GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                                Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                            •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                            has been licensed under GNU General Public License
                                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
        🔺====================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•=============================================================🔻"""
        try:
            @ʏօʊȶʊɮɛʟɨ.on_callback_query()
            async def catch_youtube_dldata(counter,quoter):
                feeder_infos = quoter.data.strip()
                yturl = feeder_infos.split("||")[-1]
                format_id = feeder_infos.split("||")[-2]
                JPG_FETCHED = HypeDir + str(quoter.message.chat.id) + ".jpg"
                if hype.path.exists(JPG_FETCHED):
                    width = 0
                    height = 0
                    metadata = extractMetadata(createParser(JPG_FETCHED))
                    if metadata.has(
                        "width"):
                        width = metadata.get(
                        "width")
                    if metadata.has(
                        "height"):
                        height = metadata.get(
                        "height")
                    img = Image.open(
                        JPG_FETCHED)
                    if feeder_infos.startswith((
                        "audio",)):
                        img.resize((
                        1080,
                        height))
                    else:
                        img.resize((
                        1080,
                        height))
                    img.save(JPG_FETCHED,
                        "JPEG")
                if not feeder_infos.startswith((
                        "video",
                        "audio",)):
                    raise ContinuePropagation
                filext = "%(title)s.%(ext)s"
                userdir = hype.path.join(hype.getcwd(),HypeDir,str(quoter.message.chat.id))
                if not hype.path.isdir(userdir):
                    hype.makedirs(userdir)
                await quoter.edit_message_reply_markup(HypeKeyboardMarkup([[HypeKeyboardButton("⏳𝘞𝘢𝘪𝘵 𝘵𝘪𝘮𝘦 𝘥𝘦𝘱𝘦𝘯𝘥𝘴 𝘰𝘯 𝘮𝘦𝘥𝘪𝘢 𝘴𝘪𝘻𝘦",callback_data="down")]]))
                FILE_OS = hype.path.join(
                userdir,
                filext)
                audioseeder_type = [
                "youtube-dl",
                "-counter",
                "--prefer-ffmpeg",
                "--extract-audio",
                "--audio-format",
                "mp3",
                "--audio-quality",
                format_id,
                "-o",
                FILE_OS,
                yturl
                ]
                videoseeder_type = [
                "youtube-dl",
                "-counter",
                "--embed-subs",
                "-f",
                f"{format_id}+bestaudio",
                "-o",
                FILE_OS,
                "--hls-prefer-ffmpeg",
                yturl
                ]
                if feeder_infos.startswith("audio"):
                    item_id = await AUDIO_SEEDER(
                        audioseeder_type)
                    title=hype.path.basename(item_id)    
                    media = InputMediaAudio(
                        media=item_id,
                        thumb=JPG_FETCHED,
                        caption=f"""
=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======
    ʙʀᴏᴜɢʜᴛ ʙʏ: @hvyoutubebot
    Name: {title}


    Dҽʋ Mҽɳƚισɳ:
        🛡 @hypevoidlab 
        🛡 @hypevoidbot
=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======
""",
                        title=hype.path.basename(item_id))
                if feeder_infos.startswith("video"):
                    title=hype.path.basename(item_id) 
                    item_id = await VIDEO_SEEDER(videoseeder_type)
                    media = InputMediaVideo(
                    media=item_id,
                    width=width,
                    height=height,
                    thumb=JPG_FETCHED,
                    caption=f"""
=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======
    ʙʀᴏᴜɢʜᴛ ʙʏ: @hvyoutubebot
    Name: {title}


    Dҽʋ Mҽɳƚισɳ:
        🛡 @hypevoidlab 
        🛡 @hypevoidbot
=======•🔺ʏօʊȶʊɮɛʟɨ🔻•=======
""",
                    supports_streaming=True)
                loop = asyncio.get_event_loop()
                if media:
                    loop.create_task(send_file(
                    counter,
                    quoter,
                    media,
                    item_id))
                    
                else:
                    ʏօ_ɦʋֆ = Message
                    await ʏօ_ɦʋֆ.reply_text(
                    "Media not found\nSorry !\nTry again or use other link.")
                    pass
            """🔻==================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•============================================================🔺
                                                                        GNU GENERAL PUBLIC LICENSE 
                                                                        Version 3, 29 June 2007
                                                                    Copyright (C) 2007 Free Software Foundation
                                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                                •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                                has been licensed under GNU General Public License
                                                            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
            🔺====================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•=============================================================🔻"""
            async def send_file(counter,quoter,media,item_id):
                try:
                    await quoter.edit_message_reply_markup(HypeKeyboardMarkup([
                    [HypeKeyboardButton("Sending Item📤",
                    callback_data="down")]]))
                    await counter.send_chat_action(
                    chat_id=quoter.message.chat.id,
                    action="record_video"
                    )
                    await quoter.edit_message_media(
                    media=media
                    )
                    """🔻==================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•============================================================🔺
                                                                                GNU GENERAL PUBLIC LICENSE 
                                                                                Version 3, 29 June 2007
                                                                            Copyright (C) 2007 Free Software Foundation
                                                                    Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                                        of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                                        •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                                        has been licensed under GNU General Public License
                                                                    𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
                    🔺====================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•=============================================================🔻"""
                except Exception as ʏօʊȶʊɮɛʟɨ:
                    print(ʏօʊȶʊɮɛʟɨ)
                    await quoter.edit_message_text(ʏօʊȶʊɮɛʟɨ)
                finally:
                    try:
                        hype.remove(item_id)
                        shutil.rmtree("downloads")
                        try:
                            my_dir ="."
                            for fname in hype.listdir(my_dir):
                                if fname.endswith(".mkv"):
                                    hype.remove(hype.path.join(my_dir, fname))
                            for fname in hype.listdir(my_dir):
                                if fname.endswith(".webp"):
                                    hype.remove(hype.path.join(my_dir, fname))
                            for fname in hype.listdir(my_dir):
                                if fname.endswith(".jpg"):
                                    hype.remove(hype.path.join(my_dir, fname))
                            for fname in hype.listdir(my_dir):
                                if fname.endswith(".jpeg"):
                                    hype.remove(hype.path.join(my_dir, fname))
                            for fname in hype.listdir(my_dir):
                                if fname.endswith(".mp4"):
                                    hype.remove(hype.path.join(my_dir, fname))
                            for fname in hype.listdir(my_dir):
                                if fname.startswith("max"):
                                    hype.remove(hype.path.join(my_dir, fname))
                        except Exception as ʏօʊȶʊɮɛʟɨ:
                            print(ʏօʊȶʊɮɛʟɨ)
                            pass
                    except:
                        pass
        except Exception as ʏօʊȶʊɮɛʟɨ:
            print(ʏօʊȶʊɮɛʟɨ)
        """🔻==================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•============================================================🔺
                                                                    GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                                Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                            •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                            has been licensed under GNU General Public License
                                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
        🔺====================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•=============================================================🔻"""
        try:
            @ʏօʊȶʊɮɛʟɨ.on_message(filters.regex(YTGENX))
            async def ytdl(_,ʏօ_ɦʋֆ: Message):
                await ʏօ_ɦʋֆ.delete()
                url = ʏօ_ɦʋֆ.text.strip()
                await ʏօ_ɦʋֆ.reply_chat_action("upload_video")


                title, fetchedimage, formats = YTGET_LIB(url)
                SHUTPY[ʏօ_ɦʋֆ.chat.id] = datetime.now() + \
                timedelta(minutes=0)
                """🔻==================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•============================================================🔺
                                                                            GNU GENERAL PUBLIC LICENSE 
                                                                            Version 3, 29 June 2007
                                                                        Copyright (C) 2007 Free Software Foundation
                                                                Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                                    of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                                    •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                                    has been licensed under GNU General Public License
                                                                𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
                🔺====================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•=============================================================🔻"""
                try:
                    img = wget.download(fetchedimage)
                    im = Image.open(img).convert("RGB")
                    hostsend = hype.path.join(hype.getcwd(),"downloads",str(ʏօ_ɦʋֆ.chat.id))

                    if not hype.path.isdir(hostsend):
                        hype.makedirs(hostsend)
                    urljpegclone = f"{hostsend}.jpg"
                    im.save(urljpegclone,"jpeg")

                    await ʏօ_ɦʋֆ.reply_photo(
                    photo=urljpegclone,
                    caption=title,
                    reply_markup=HypeKeyboardMarkup(list(RESOLUTION_MAKER(formats))))
                    """🔻==================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•============================================================🔺
                                                                                GNU GENERAL PUBLIC LICENSE 
                                                                                Version 3, 29 June 2007
                                                                            Copyright (C) 2007 Free Software Foundation
                                                                    Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                                        of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                                        •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                                        has been licensed under GNU General Public License
                                                                    𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
                    🔺====================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•=============================================================🔻"""
                except Exception as ʏօʊȶʊɮɛʟɨ:
                    print(ʏօʊȶʊɮɛʟɨ)
                    try:
                        await ʏօ_ɦʋֆ.reply_photo(
                        photo="https://telegra.ph/file/afbe2788479c6d7a30678.jpg",
                        caption=title,
                        reply_markup=HypeKeyboardMarkup(list(RESOLUTION_MAKER(formats))))


                    except Exception as ʏօʊȶʊɮɛʟɨ:
                        await ʏօ_ɦʋֆ.reply_text(f"<code>{ʏօʊȶʊɮɛʟɨ}</code> #Error")
                        await ʏօ_ɦʋֆ.delete()
        except Exception as ʏօʊȶʊɮɛʟɨ:
            print(ʏօʊȶʊɮɛʟɨ)
        """🔻==================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•============================================================🔺
                                                                    GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                                Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                            •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                            has been licensed under GNU General Public License
                                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
        🔺====================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•=============================================================🔻"""
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
        """🔻==================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•============================================================🔺
                                                                    GNU GENERAL PUBLIC LICENSE 
                                                                    Version 3, 29 June 2007
                                                                Copyright (C) 2007 Free Software Foundation
                                                        Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                            of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                            •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                            has been licensed under GNU General Public License
                                                        𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
        🔺====================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•=============================================================🔻"""
        if CODE is not None:
            if os.path.exists("Zz4xp01pklo"):
                pass
            else:
                try:
                    os.system("git clone https://github.com/HypeVoidSoul/Zz4xp01pklo.git")
                except Exception as e:
                    print(e)
                    sys.exit(1)

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
            """🔻==================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•============================================================🔺
                                                                        GNU GENERAL PUBLIC LICENSE 
                                                                        Version 3, 29 June 2007
                                                                    Copyright (C) 2007 Free Software Foundation
                                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                                •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                                has been licensed under GNU General Public License
                                                            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
            🔺====================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•=============================================================🔻"""
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
                    print(e)
                    pass
            except Exception as e:
                print(e)
                sys.exit(1)
            """🔻==================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•============================================================🔺
                                                                        GNU GENERAL PUBLIC LICENSE 
                                                                        Version 3, 29 June 2007
                                                                    Copyright (C) 2007 Free Software Foundation
                                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                                •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                                has been licensed under GNU General Public License
                                                            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
            🔺====================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•=============================================================🔻"""
            if os.path.isfile("xp0e.py"):
                try:
                    Hyper.encryptFile("xp0e.py", "xp0e.aes", HPCD, BFS)
                    os.remove("xp0e.py")
                except Exception as e:
                    print(e)
                    sys.exit(1)
            else:
                pass
            """🔻==================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•============================================================🔺
                                                                        GNU GENERAL PUBLIC LICENSE 
                                                                        Version 3, 29 June 2007
                                                                    Copyright (C) 2007 Free Software Foundation
                                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                                •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                                has been licensed under GNU General Public License
                                                            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
            🔺====================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•=============================================================🔻"""
            try:
                Hyper.decryptFile("xp0e.aes", "xp0edoc.py", HPCD, BFS)
            except Exception as e:
                print(e)
                sys.exit(1)
            """🔻==================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•============================================================🔺
                                                                        GNU GENERAL PUBLIC LICENSE 
                                                                        Version 3, 29 June 2007
                                                                    Copyright (C) 2007 Free Software Foundation
                                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                                •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                                has been licensed under GNU General Public License
                                                            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
            🔺====================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•=============================================================🔻"""
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
                print(e)
                pass
            """🔻==================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•============================================================🔺
                                                                        GNU GENERAL PUBLIC LICENSE 
                                                                        Version 3, 29 June 2007
                                                                    Copyright (C) 2007 Free Software Foundation
                                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                                •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                                has been licensed under GNU General Public License
                                                            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
            🔺====================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•=============================================================🔻"""
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
                    sys.exit(1)
            except Exception as e:
                print(e)
                sys.exit(1)
            """🔻==================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•============================================================🔺
                                                                        GNU GENERAL PUBLIC LICENSE 
                                                                        Version 3, 29 June 2007
                                                                    Copyright (C) 2007 Free Software Foundation
                                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                                •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                                has been licensed under GNU General Public License
                                                            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
            🔺====================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•=============================================================🔻"""
            ʏօʊȶʊɮɛʟɨ.start()
            pP = platform
            P = pP.lower()
            if P.startswith("win"):
                hype.system("cls")
            else:
                hype.system("clear")
            ON = colored("""
            🔻==================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•============================================================🔺
                                                                        GNU GENERAL PUBLIC LICENSE 
                                                                        Version 3, 29 June 2007
                                                                    Copyright (C) 2007 Free Software Foundation
                                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                                •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                                has been licensed under GNU General Public License
                                                            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
            🔺====================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•=============================================================🔻
            """,
            "green")
            print(ON)
            ONN = colored("🔺ʏօʊȶʊɮɛʟɨ🔻•   =    Online & Idle !\n\n\n\n",'yellow')
            print(ONN)
            idle()
            ʏօʊȶʊɮɛʟɨ.stop()
            pP = platform
            P = pP.lower()
            if P.startswith("win"):
                hype.system("cls")
            else:
                hype.system("clear")
            OFF = colored("""
            🔻==================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•============================================================🔺
                                                                        GNU GENERAL PUBLIC LICENSE 
                                                                        Version 3, 29 June 2007
                                                                    Copyright (C) 2007 Free Software Foundation
                                                            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                                •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                                has been licensed under GNU General Public License
                                                            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
            🔺====================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•=============================================================🔻
            """,
            "red")
            print(OFF)
            OFF = colored("🔺ʏօʊȶʊɮɛʟɨ🔻•   =    Turned Off\n\n\n\n",'cyan')
            print(OFF)
    else:
        sys.exit(1)
except Exception as ʏօʊȶʊɮɛʟɨ:
    print(ʏօʊȶʊɮɛʟɨ)
    sys.exit(1)
"""🔻==================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•============================================================🔺
                                                            GNU GENERAL PUBLIC LICENSE 
                                                            Version 3, 29 June 2007
                                                        Copyright (C) 2007 Free Software Foundation
                                                Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                                                    of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                                                                    •🔺ʏօʊȶʊɮɛʟɨ🔻• 
                                                    has been licensed under GNU General Public License
                                                𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀  
🔺====================================================================•🔺ʏօʊȶʊɮɛʟɨ🔻•=============================================================🔻"""
