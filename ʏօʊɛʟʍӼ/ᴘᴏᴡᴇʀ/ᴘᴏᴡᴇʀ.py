from Cula import *

@ɦֆ.on_message(
    filters.private
    &filters.command(
    "start",
    prefixes='/')) 
def start(_,ɦʋֆ: Message):
    usrs = ɦʋֆ.from_user.first_name
    joinButton = InlineKeyboardMarkup([
                                    [InlineKeyboardButton("🍺 Grðµþ:",url="https://t.me/hypevoids")],
                                    [InlineKeyboardButton("📡 ßð†§ Hµß:",url="https://t.me/hypevoidlab")],
                                    [InlineKeyboardButton("🛡 ÇðÐêß¥",url="https://t.me/HypeVoidSoul")]
                                    ])
    
    welcomed = f"""
🍟==========『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==========🍟

🎈Dear,
Sir,Ma'am  <b>{usrs}</b>

Use the below button or type /help for More info.

🍟==========『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==========🍟
"""
    
    ɦʋֆ.reply_photo(
        "https://telegra.ph/file/309fa4e4bdae98dd658c1.jpg",
        caption=welcomed,
        reply_markup=joinButton)
    raise StopPropagation
