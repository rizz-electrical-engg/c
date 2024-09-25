import logging
import os
import time
from io import BytesIO, StringIO
from logging.handlers import RotatingFileHandler

from dotenv import load_dotenv
from pyrogram import Client

botStartTime = time.time()

if os.path.exists('BindhuEncoder/config.env'):
    load_dotenv('BindhuEncoder/config.env')

# Variables

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")

database = os.environ.get("MONGO_URI")
session = os.environ.get("MONGO_DB_NAME")

drive_dir = os.environ.get("DRIVE_DIR")
index = os.environ.get("INDEX_URL")

download_dir = os.environ.get("DOWNLOAD_DIR")
encode_dir = os.environ.get("ENCODE_DIR")

owner = list(set(int(x) for x in os.environ.get("OWNER_ID").split()))
sudo_users = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))
everyone = list(set(int(x) for x in os.environ.get("EVERYONE_CHATS").split()))
all = everyone + sudo_users + owner

try:
    log = int(os.environ.get("LOG_CHANNEL"))
except:
    log = owner
    print('Fill logs id 😞!')


data = []

PROGRESS = """
• {0} of {1}
• Speed: {2}
• ETA: {3}
"""

video_mimetype = [
    "video/x-flv",
    "video/mp4",
    "application/x-mpegURL",
    "video/MP2T",
    "video/3gpp",
    "video/quicktime",
    "video/x-msvideo",
    "video/x-ms-wmv",
    "video/x-matroska",
    "video/webm",
    "video/x-m4v",
    "video/quicktime",
    "video/mpeg"
]

def memory_file(name=None, contents=None, *, bytes=True):
    if isinstance(contents, str) and bytes:
        contents = contents.encode()
    file = BytesIO() if bytes else StringIO()
    if name:
        file.name = name
    if contents:
        file.write(contents)
        file.seek(0)
    return file

# Check Folder
if not os.path.isdir(download_dir):
    os.makedirs(download_dir)
if not os.path.isdir(encode_dir):
    os.makedirs(encode_dir)

# the logging things
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            'BindhuEncoder/utils/extras/logs.txt',
            backupCount=20
        ),
        logging.StreamHandler()
    ]
)

logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

# Client
app = Client(
    session,
    bot_token=bot_token,
    api_id=api_id,
    api_hash=api_hash,
    plugins={'root': os.path.join(__package__, 'plugins')},
    sleep_threshold=30)
