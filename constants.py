from os import environ
from dotenv import load_dotenv

load_dotenv()

VK_PASSWORD = environ.get("VK_PASSWORD")
VK_LOGIN = environ.get("VK_LOGIN")
VK_TOKEN = environ.get("VK_TOKEN")
VK_API_VERSION = environ.get("VK_API_VERSION")
LAST_MAX_ID = environ.get("LAST_MAX_ID")
