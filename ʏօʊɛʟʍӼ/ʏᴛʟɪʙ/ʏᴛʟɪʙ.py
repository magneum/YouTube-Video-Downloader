from UIYTRQAMCYTWADDALPPOWFVMAS import *
from ɴᴜᴋᴏʟᴀ import *
from ʏօʊȶʊɮɛʟɨ import *
from Cula import *

@Client.on_message(
filters.regex(
YTGENX))
async def ytdl(_,ɦʋֆ: Message):
    url = ɦʋֆ.text.strip()
    await ɦʋֆ.reply_chat_action(CRAV)
    await ɦʋֆ.delete()
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
            nonimg = "https://telegra.ph/file/309fa4e4bdae98dd658c1.jpg"
            await ɦʋֆ.reply_photo(
                nonimg,
                caption=title,
                reply_markup=pod)
        except Exception as e:
            await ɦʋֆ.reply_text(
            f"<code>{e}</code> #Error")
            await ɦʋֆ.delete()
