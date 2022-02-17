import requests
from .config import *

def send_message(msg):
    requests.get(f'{BASE}{TOKEN}{SEND_MSG_API}?chat_id={CHAN_ID}&text={msg}')

send_message('it works!')