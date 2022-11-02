from os import environ
from dotenv import load_dotenv

load_dotenv()

VK_PASSWORD = environ.get('VK_PASSWORD')
VK_LOGIN = environ.get('VK_LOGIN')
