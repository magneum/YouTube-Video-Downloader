from Cula import *
class Kryogenesis(object):
    YOUELMX = os.environ.get("YOUELMX")
    TOKEN = os.environ.get("TOKEN")
    APP_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
class Hypotherm(Kryogenesis):
    LOGGER = True