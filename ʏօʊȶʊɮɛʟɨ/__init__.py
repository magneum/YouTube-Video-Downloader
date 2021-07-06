from logging import INFO, basicConfig, getLogger
basicConfig(
format="%(levelname)s - %(message)s",
level=INFO)
LOGS = getLogger(__name__)
from pyrogram import (
    Client as ɦֆʋ,
    idle
    )
from ʟaʄɨօ import *

plugins = dict(
    root="ʏօʊɛʟʍӼ",
)
TOKEN = Kryogenesis.TOKEN
APP_ID = Kryogenesis.APP_ID
API_HASH = Kryogenesis.API_HASH

ɦʋֆ = ɦֆʋ(
    session_name="ɦʋֆ",
    bot_token=TOKEN,
    api_id=APP_ID,
    api_hash=API_HASH,
    plugins=plugins,
    workers=12
    )