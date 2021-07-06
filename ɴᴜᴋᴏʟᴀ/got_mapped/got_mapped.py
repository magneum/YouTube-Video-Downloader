from ᴠʏᴛᴇꜱᴠɪʟᴇ import *
from pyrogram.types import (
    InlineKeyboardButton,
    )


def got_mapped(fetchedfiles):
    resolution = fetchedfiles['format']
    if "audio" in resolution:
        return [
        InlineKeyboardButton(
        f"🎧{resolution}🍩{ᴠʏᴛᴇꜱᴠɪʟᴇ(fetchedfiles['filesize'])}🍩",
        callback_data=f"ytdata||audio||{fetchedfiles['format_id']}||{fetchedfiles['yturl']}")]
    else:
        return [
        InlineKeyboardButton(
        f"🎬{resolution}🍿{ᴠʏᴛᴇꜱᴠɪʟᴇ(fetchedfiles['filesize'])}🍿",
        callback_data=f"ytdata||video||{fetchedfiles['format_id']}||{fetchedfiles['yturl']}")]

def resmaker(resolutiontree):
    return map(got_mapped, resolutiontree)
