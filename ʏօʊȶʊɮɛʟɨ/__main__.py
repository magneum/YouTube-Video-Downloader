from pyrogram.methods.utilities import idle
from Cula import *
from ʟaʄɨօ import *

plugins = dict(
    root="ʏօʊɛʟʍӼ",
)
TOKEN = Kryogenesis.TOKEN
APP_ID = Kryogenesis.APP_ID
API_HASH = Kryogenesis.API_HASH

Client = Client(
    session_name="ɦʋֆ",
    bot_token=TOKEN,
    api_id=APP_ID,
    api_hash=API_HASH,
    plugins=plugins,
    workers=12
    )


Client.start()
idle()
try:
    shutil.rmtree(K)
    shutil.rmtree(P)
    shutil.rmtree(V)
    shutil.rmtree(Y)
    shutil.rmtree(M)
except:
    pass
Client.stop()
