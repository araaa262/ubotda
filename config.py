;import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "1000"))

DEVS = list(map(int, os.getenv("DEVS", "1701447702").split()))

API_ID = int(os.getenv("API_ID", "22286411"))

API_HASH = os.getenv("API_HASH", "e85b709fac1b34b677768bb8d25dd487")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8229730883:AAFmgOTI9_siBFC3oiWLBdhOPc_7T4w9R5A")

OWNER_ID = int(os.getenv("OWNER_ID", "1701447702"))

BLACKLIST_CHAT = list(map(int, os.getenv("").split()))

RMBG_API = os.getenv("RMBG_API", "KTy4y85AwucHk4czmW8EDEq1")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://linsstore0_db_user:linda123#@linda0.ldzurtw.mongodb.net/?retryWrites=true&w=majority&appName=linda0")
LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-4628173231"))
