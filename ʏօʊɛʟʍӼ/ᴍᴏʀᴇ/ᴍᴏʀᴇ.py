from Cula import *

@ɦֆ.on_message(filters.command(
    "help",
    prefixes='/')) 
async def help(_,ɦʋֆ: Message):
    usrs = ɦʋֆ.from_user.first_name
    MORETITE = f"""
🍟==========『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==========🍟
🎈Dear <b>**{usrs}**</b>

Using `YouTube Audio/Video Downloader` bot is very simple.
Just follow these points and you will be good to go.

- Initially send a valid Youtube Link (don't forward!)
- Bot will serve you all the available options to download the file.
- Choose the `Audio/Video and The Resolution`.
- Wait till it gets downloaded and repeat untill ur appetite is satisfied.


Dҽʋ Mҽɳƚισɳ: @HypeVoidBot
🍟==========『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==========🍟
"""
       
    await ɦʋֆ.reply_photo(
        "https://telegra.ph/file/309fa4e4bdae98dd658c1.jpg",
        caption=MORETITE)
    raise StopPropagation
